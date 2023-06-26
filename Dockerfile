ARG PYTHON_VERSION

FROM python:${PYTHON_VERSION}-slim-bullseye
LABEL maintainer="victormiti@umusebo.com"
LABEL version="${PYTHON_VERSION}"
LABEL description="Python ${PYTHON_VERSION}-slim-bullseye plus texlive and pandoc"

RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
    texlive-full \
    pandoc \
    ; \
    rm -rf /var/lib/apt/lists/*

CMD ["python3"]
