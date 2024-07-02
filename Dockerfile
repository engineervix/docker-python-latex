ARG PYTHON_VERSION
ARG DEBIAN_VERSION

FROM python:${PYTHON_VERSION}-slim-${DEBIAN_VERSION}
LABEL maintainer="hello@victor.co.zm"

# we're redefining this because Docker labels don't directly support variable substitution
# By redefining the arguments after the `FROM` directive,
# Docker can substitute their values correctly when setting the labels
ARG PYTHON_VERSION
ARG DEBIAN_VERSION

LABEL version="${PYTHON_VERSION}-slim-${DEBIAN_VERSION}"
LABEL description="Python ${PYTHON_VERSION}-slim-${DEBIAN_VERSION} plus texlive-full (without the docs) and pandoc"

RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
    # https://gist.github.com/wkrea/b91e3d14f35d741cf6b05e57dfad8faf
    `apt --assume-no install texlive-full | \
    awk '/The following additional packages will be installed/{f=1;next} /Suggested packages/{f=0} f' | \
    tr ' ' '\n' | \
    grep -vP 'doc$' | \
    tr '\n' ' '` \
    pandoc \
    ; \
    rm -rf /var/lib/apt/lists/*

CMD ["python3"]