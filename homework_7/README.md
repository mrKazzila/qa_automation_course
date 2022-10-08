Домашнее задание №7
=====

## Цель:
- Научиться внедрять в проект логгирование и отчётность allure.

### Описание:
- Настройте логирование внутри PageObject'ов. (черед модуль logging).
- Добавьте аннотации для шагов и тестов для трансляции в отчёт Allure.
- Настройте Selenoid, добавьте несколько браузеров и запустите на них тесты.
- Предусмотрите возможность запуска тестов как на удаленных сервисах так и локально.
- Предусмотрите снятие скриншота и добавление его в отчёт при падении тестов.

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
qa_automation_course>cd homework_7
```

3. Запуск скрипта
```shell script
qa_automation_course/homework_7>pytest
```

4. Генерация Allure отчета
```shell script
<Ваш путь до файла allure.bat> generate
```
