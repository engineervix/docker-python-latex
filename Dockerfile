FROM python:3.11-slim-bullseye
LABEL maintainer="victormiti@umusebo.com"
LABEL description="Python 3.10-slim-bullseye plus texlive and pandoc"

RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
    texlive-full \
    pandoc \
    ; \
    rm -rf /var/lib/apt/lists/*

CMD ["python3"]
