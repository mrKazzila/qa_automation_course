FROM python:3.11-slim-buster

WORKDIR /homework_04

COPY . .

RUN pip install -U pip && pip install pytest \
    && pip install pydantic \
    && pip install requests

CMD ["pytest"]
