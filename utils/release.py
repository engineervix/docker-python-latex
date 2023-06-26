#!/usr/bin/env python3

"""release.py

to help in managing releases using `standard-version`_.

Usage in this project:
    python misc/release.py [bump | notes]

.. _standard-version: https://github.com/conventional-changelog/standard-version
"""

import argparse
import os
import subprocess
import sys

# from pathlib import Path

# colorama is a commitizen dependency
from colorama import Fore, init


def get_first_commit():
    try:
        output = subprocess.check_output(
            ["git", "log", "--reverse", "--format=%H", "--max-parents=0"],
            universal_newlines=True,
        )
        return output.strip()
    except subprocess.CalledProcessError:
        return None


def execute_bump_hack(branch, is_first_release=False, major=False):
    """A little hack that combines commitizen-tools and standard-version

    commitizen-tools works best with Python projects, but I don't like the
    generated changelogs. I had no time to look at how to customize them, so I
    decided to use standard-version (which works best with Node.js projects).
    Unfortunately, standard-version by default doesn't work with Python projects,
    and since I didn't have time to write my own updater for python files and toml files,
    I have to make the two work together!

    This requires standard-version to be installed in your project:
    ``npm i -D standard-version``
    If you're setting it up for the first time on another project, you will probably
    encounter problems generating the entire changelog. See how Łukasz Nojek came up
    with a hack to deal with this:
    https://lukasznojek.com/blog/2020/03/how-to-regenerate-changelog-using-standard-version/

    The formula (workflow) for is as follows:

    1. cz bump --files-only
    2. git add pyproject.toml and other_files specified in pyproject.toml
    3. standard-version --commit-all --release-as <result from cz if not none>
    4. git push --follow-tags origin [branch]
    """
    if is_first_release:
        first_commit = get_first_commit()
        if first_commit:
            os.system(f"git checkout {first_commit}")
            os.system('GIT_COMMITTER_DATE="$(git show --format=%aD | head -1)"')
            os.system('git tag -a v0.0.0 -m "v0.0.0 - this is where it all starts"')
            os.system("unset GIT_COMMITTER_DATE")
            os.system(f"git checkout {branch}")
            release_type = "major" if major else "minor"
            os.system(f"cz bump --files-only --increment {release_type.upper()}")
            os.system("git add .cz.toml")
            os.system(
                f'npm run release -- --commit-all --release-as {release_type} --releaseCommitMessageFormat "chore: This is zed-shipping v{{{{currentTag}}}} 🎉"'
            )
            # push to origin
            os.system(f"git push --follow-tags origin {branch}")
        else:
            print("No commit found or Git repository not initialized.")
    else:
        print(
            f"{Fore.MAGENTA}Attempting to bump using commitizen-tools ...{Fore.RESET}"
        )
        os.system("cz bump --files-only > .bump_result.txt")
        str_of_interest = "increment detected: "
        result = ""
        with open(".bump_result.txt", "r") as br:
            for line in br:
                if str_of_interest in line:
                    result = line
                    break
        release_type = result.replace(str_of_interest, "").strip("\n").lower()
        print(f"cz bump result: {release_type}")
        if release_type == "none":
            print(f"{Fore.YELLOW}No increment detected, cannot bump{Fore.RESET}")
        elif release_type in ["major", "minor", "patch"]:
            print(f"{Fore.GREEN}Looks like the bump command worked!{Fore.RESET}")
            print(f"{Fore.GREEN}Now handing over to standard-version ...{Fore.RESET}")
            # first, stage the bumped files
            os.system("git add .cz.toml")
            # now we can pass result to standard-release
            print(
                f"{Fore.GREEN}let me retrieve the tag we're bumping from ...{Fore.RESET}"
            )
            get_current_tag = subprocess.getoutput(
                "git describe --abbrev=0 --tags `git rev-list --tags --skip=0  --max-count=1`"
            )
            previous_tag = get_current_tag.rstrip()
            os.system(
                f'npm run release -- --commit-all --release-as {release_type} --releaseCommitMessageFormat "bump: ✈️ {previous_tag} → v{{{{currentTag}}}}"'
            )
            # push to origin
            os.system(f"git push --follow-tags origin {branch}")
        else:
            print(
                f"{Fore.RED}Something went horribly wrong, please investigate & fix it!{Fore.RESET}"
            )
            print(f"{Fore.RED}Bump failed!{Fore.RESET}")

        # clean up
        os.system("rm -vf .bump_result.txt")


def get_release_notes():
    """extract content from CHANGELOG.md for use in Github Releases

    we read the file and loop through line by line
    we wanna extract content beginning from the first Heading 2 text
    to the last line before the next Heading 2 text
    """
    pattern_to_match = "## [v"

    count = 0
    lines = []
    heading_text = "## What's changed in this release\n"
    lines.append(heading_text)

    with open("CHANGELOG.md", "r") as c:
        for line in c:
            if pattern_to_match in line and count == 0:
                count += 1
            elif pattern_to_match not in line and count == 1:
                lines.append(line)
            elif pattern_to_match in line and count == 1:
                break

    # home = str(Path.home())
    # release_notes = os.path.join(home, "LATEST_RELEASE_NOTES.md")
    release_notes = os.path.join("../", "LATEST_RELEASE_NOTES.md")
    with open(release_notes, "w") as f:
        print("".join(lines), file=f, end="")


def release(args=None):
    """Console script entry point"""

    if not args:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser(
        prog="release",
        description="to help in managing releases using standard-version",
    )

    parser.add_argument(
        "operation", help="The operation to perform [ bump | notes ].", type=str
    )

    parser.add_argument(
        "--first-release",
        dest="first_release",
        action="store_true",
        help="Create the first release.",
    )

    parser.add_argument(
        "--major",
        dest="major",
        action="store_true",
        help="Create a major release.",
    )

    args = parser.parse_args(args)

    init()

    if args.operation in ["bump", "notes"]:
        if args.operation == "bump":
            first = args.first_release
            major = args.major
            execute_bump_hack(branch="main", is_first_release=first, major=major)
        else:
            get_release_notes()
    else:
        print("accepted operations: bump | notes")
        print("please try again")
        sys.exit(1)


if __name__ == "__main__":
    unstaged_str = "not staged for commit"
    uncommitted_str = "to be committed"
    check = subprocess.getoutput("git status")
    if unstaged_str not in check or uncommitted_str not in check:
        release()
    else:
        print("Sorry mate, please ensure there are no pending git operations")