ARG DEBIAN_VERSION
ARG PYTHON_VERSION

FROM python:${PYTHON_VERSION}-slim-${DEBIAN_VERSION}
LABEL maintainer="victormiti@umusebo.com"
LABEL version="${PYTHON_VERSION}"
LABEL description="Python ${PYTHON_VERSION}-slim-${DEBIAN_VERSION} plus texlive and pandoc"

RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
    texlive-full \
    pandoc \
    ; \
    rm -rf /var/lib/apt/lists/*

CMD ["python3"]
