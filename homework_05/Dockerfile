FROM python:3.10-slim-buster

WORKDIR /homework_05

COPY . .

RUN pip install -U pip && pip install pytest==7.1.2 \
    && pip install selenium==4.1.3 \
    && pip install webdriver-manager

CMD ["pytest", "-v"]
