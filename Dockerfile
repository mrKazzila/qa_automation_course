FROM python:3.8

WORKDIR /app

COPY requirements.txt .

RUN pip install -U pip && pip install -r requirements.txt

COPY homework_7 .

CMD ["pytest", "--executor", "192.168.0.179", "--url","http://192.168.0.179:8081/", "--vnc", "tests/test_main_page.py"]