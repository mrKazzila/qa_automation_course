FROM python:3.11-slim as poetry

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_ROOT_USER_ACTION=ignore

WORKDIR /app

COPY ./poetry.lock ./pyproject.toml ./

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        # deps for installing poetry
        curl \
    \
    # install poetry
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python \
    && export PATH="/root/.local/bin:$PATH" \
    && poetry export --without-hashes --format=requirements.txt > ./requirements.txt \
    && rm -rf var/cache


FROM poetry as venv

WORKDIR /homework_07
COPY --from=poetry ./app/requirements.txt ./requirements.txt

RUN pip install --upgrade pip \
    && pip install -r ./requirements.txt \
    && rm -rf app/

COPY ./homework_07 .


FROM venv as runtime

COPY --from=venv ./homework_07/ ./

CMD ["pytest"]