# Multistage build
# 1. Base image as python for requirements/env
FROM python:3.8-slim as base

RUN apt-get update \
&& apt-get install -y --no-install-recommends git \
&& apt-get purge -y --auto-remove \
&& rm -rf /var/lib/apt/lists/*

FROM base as dependencies

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

RUN python -m venv /opt/venv
# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"


RUN pip install poetry==1.1.7 && \
    poetry config virtualenvs.create false

# copy poetry packages file
COPY pyproject.toml ./
RUN poetry install --no-interaction --no-ansi
RUN pip3 install python-dateutil
# Multistage build
# 2. Changes from the backend files
FROM base as final

# copy installed deps from dependencies image
COPY --from=dependencies /opt/venv /opt/venv
# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"

EXPOSE 8001
WORKDIR /app

# copying working files at workdir
# Django
COPY manage.py .
COPY config config
COPY apps apps

# Entrypoint script
COPY ./scripts/run.sh .

# Linting flake8
COPY tox.ini .

# Make file executable
RUN chmod +x run.sh

RUN mkdir static

# Entrypoint
CMD ["/app/run.sh"]
