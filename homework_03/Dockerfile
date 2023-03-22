FROM python:3.11-slim-buster

WORKDIR /homework_03

COPY . .

RUN pip install -U pip

CMD ["python3", "./app/main.py", "-u", "./data/users.json", "-b", "./data/books.csv", "-r", "./result.json"]
CMD ["ls"]