FROM python:3.10-slim-buster

RUN apt-get update && apt-get install -y procps && rm -rf /var/lib/apt/lists/*

WORKDIR /homework_08

COPY . .

RUN pip install -U pip

CMD ["python3", "./app/main.py"]