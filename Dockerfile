ARG PYTHON_VERSION
ARG DEBIAN_VERSION

FROM python:${PYTHON_VERSION}-slim-${DEBIAN_VERSION}
LABEL maintainer="hello@victor.co.zm"
LABEL version="${PYTHON_VERSION}-slim-${DEBIAN_VERSION}"
LABEL description="Python ${PYTHON_VERSION}-slim-${DEBIAN_VERSION} plus texlive-full and pandoc"

RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
    texlive-full \
    pandoc \
    ; \
    rm -rf /var/lib/apt/lists/*

CMD ["python3"]
