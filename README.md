# python-latex

[![Build Docker images](https://github.com/engineervix/docker-python-latex/actions/workflows/build-docker-image.yml/badge.svg)](https://github.com/engineervix/docker-python-latex/actions/workflows/build-docker-image.yml)
[![Publish Docker images](https://github.com/engineervix/docker-python-latex/actions/workflows/publish-docker-image.yml/badge.svg)](https://github.com/engineervix/docker-python-latex/actions/workflows/publish-docker-image.yml)

> A Docker image to ease building Python applications that depend on [LaTeX](https://www.latex-project.org/)

## Features

- Python 3.8 - 3.12, based on the official `slim-*` images, where `*` includes:
  - `bullseye`
  - `bookworm`
- LaTeX environment with `texlive-full`
- [Pandoc](https://pandoc.org/) for converting from one markup format to another

## Usage

### Pulling the Image

You can pull the pre-built image from Docker Hub:

```sh
docker pull engineervix/python-latex:3.12-slim-bookworm
```

Replace `3.12` and `bookworm` with the desired Python version and Debian release, respectively.

### Running a Container

To run a container using the image:

```sh
docker run -it --rm engineervix/python-latex:3.12-slim-bookworm
```

This will start an interactive shell inside the container.

### Building a Container with Your Application

Here's an example of a `Dockerfile` for your Python application:

```dockerfile
FROM engineervix/python-latex:3.12-slim-bookworm

WORKDIR /app

# Copy your application files
COPY . /app

# Install any necessary dependencies
RUN pip install -r requirements.txt

# Command to run your application
CMD ["python", "your_script.py"]
```

Build and run your container:

```sh
docker build -t my-python-latex-app .
docker run -it --rm my-python-latex-app
```

### Using LaTeX and Pandoc

You can directly use LaTeX and Pandoc commands within the container. For example, to convert a Markdown file to a PDF:

1. Start a container and mount your current directory:

```sh
docker run -it --rm -v $(pwd):/workspace -w /workspace engineervix/python-latex:3.12-slim-bookworm
```

2. Inside the container, use Pandoc to convert your file:

```sh
pandoc input.md -o output.pdf
```

Or compile a LaTeX document:

```sh
pdflatex document.tex
```
