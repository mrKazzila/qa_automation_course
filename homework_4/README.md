Домашнее задание №4
=====

## Цель:
- Поучиться тестировать API сервисов на основе их документации.

## Описание:
Тестирование каждого api оформить в отдельном тестовом модуле.

1. Тестирование REST сервиса https://dog.ceo/dog-api/
2. Тестирование REST сервиса https://www.openbrewerydb.org/
3. Тестирование REST сервиса https://jsonplaceholder.typicode.com/

#### Критерии
- Для каждого REST сервиса написать минимум 5 тестов.
- Как минимум 2 из 5 должны использовать параметризацию.
- Тесты должны проходить успешно.

Реализуйте в отдельном модуле тестовую функцию которая будет принимать 2 параметра:
- url - должно быть значение по умолчанию https://ya.ru
- status_code - значение по умолчанию 200

#### Критерии 
- Параметры должны быть реализованы через pytest.addoption.
- Можно положить фикcтуру и тестовую функцию в один файл.
Основная задача чтобы ваш тест проверял по переданному урлу статус ответа тот который передали,
т.е. по адресу https://ya.ru/sfhfhfhfhfhfhfhfh должен быть валидным ответ 404
пример запуска pytest test_module.py --url=https://mail.ru --status_code=200

## Запуск:
0. Создание виртуального окружения.
```shell script
qa_automation_course>python -m venv venv
```

1. Активация виртуального окружения.
```shell script
qa_automation_course>cd venv/Scripts
qa_automation_course/venv/Scripts>activate
qa_automation_course/venv/Scripts> cd ../..
qa_automation_course>pip install -r requirements.txt
``` 

2. Переход в рабочую директорию.
```shell script
qa_automation_course>cd homework_4
```

3. Запуск скрипта
```shell script
qa_automation_course/homework_4>pytest [OPTIONS]
```

**Параметры:**

| Параметр  |  Описание | Значение по умолчанию |
| ------------- | ------------- | ------------- |
| `Dog_api` | Запуск тестов для сервиса https://dog.ceo/dog-api/ | Необязательный параметр |
| `Jsonplaceholder` | Запуск тестов для сервиса https://jsonplaceholder.typicode.com/ | Необязательный параметр |
| `Open_brewery_db` | Запуск тестов для сервиса https://www.openbrewerydb.org/ | Необязательный параметр |
| `test_validation_status_code.py` | Запуск теста для валидации status_code | Необязательный параметр |
