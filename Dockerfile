FROM oz123/pipenv:3.10-2023.07.23 AS builder

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

ENV PIPENV_VENV_IN_PROJECT=1

ADD Pipfile.lock Pipfile /usr/src/

WORKDIR /usr/src

RUN pipenv sync

FROM python:3.10-slim-buster as runtime

RUN apt-get update && apt-get install -y supervisor

RUN useradd --create-home developer
WORKDIR /home/developer
USER developer

COPY --from=builder /usr/src/.venv/ .venv/
COPY . .

ENTRYPOINT ["/usr/bin/supervisord"]
