Домашнее задание №6
=====

## Цель:
- Научиться реализовывать PageObject шаблон в автотестах.

### Описание:

- Переписать уже имеющиеся тесты в проекта opencart на PageObject паттерн.
- Добавить автотесты на следующие сценарии.
  - Добавление нового товара в разделе администратора.
  - Удаление товара из списка в разделе администартора.
  - Регистрация нового пользователя в магазине опенкарта.
  - Переключение валют из верхнего меню опенкарта.

### Запуск:
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
qa_automation_course>cd homework_6
```

3. Запуск скрипта
```shell script
qa_automation_course/homework_6>pytest
```
