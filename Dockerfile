FROM --platform=linux/amd64 ubuntu:18.04

ENV DEBIAN_FRONTEND noninteractive
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

ARG USER_ID
ARG GROUP_ID
ARG PYTHON_VERSION=3.10.8

RUN (addgroup --gid $GROUP_ID app || true) \
    && adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID app

ENV HOME /home/app
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV PYTHONPATH=/app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHON=python
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH
ENV NVM_DIR /usr/local/nvm
ENV NODE_VERSION 16.19.0

RUN apt-get update \
    && apt-get install -y git curl wget \
    zlib1g zlib1g-dev python3-pip libssl-dev \
    bzip2 libbz2-dev sqlite3 libsqlite3-dev \
    libreadline-dev libffi-dev liblzma-dev \
    python-dev build-essential

RUN mkdir -p $NVM_DIR \
    && curl https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash \
    && . $NVM_DIR/nvm.sh \
    && nvm install $NODE_VERSION \
    && nvm alias default $NODE_VERSION \
    && nvm use default

ENV NODE_PATH $NVM_DIR/versions/node/v$NODE_VERSION/lib/node_modules
ENV PATH      $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH

USER app
WORKDIR /app

RUN git clone https://github.com/pyenv/pyenv.git $HOME/.pyenv \
    && env PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install $PYTHON_VERSION \
    && pyenv global $PYTHON_VERSION \
    && pip install --upgrade pip \
    && pip install poetry \
    && poetry config virtualenvs.create false

ENV PATH="${PATH}:${HOME}/.local/bin"
ENV PATH $PYENV_ROOT/versions/$PYTHON_VERSION/bin:$PATH

COPY pyproject.toml poetry.lock* /app/

RUN poetry install
RUN npm install create-vue@3.5.0
