import csv
import json
from typing import List

from settings import CountInfo


def read_data_with_users(file_name: str) -> List[dict]:
    """
    Читаем файл с данными пользователей

    :param file_name: Путь до файла с пользователями
    """
    with open(file_name, 'r') as json_data:
        users = json.load(json_data)
        CountInfo.COUNT_USERS = len(users)

        return [
            {
                'name': user.get('name'),
                'gender': user.get('gender'),
                'address': user.get('address'),
                'age': user.get('age'),
                'books': [],
            }
            for user in users
        ]


def read_data_with_books(file_name: str) -> List[dict]:
    """
    Читаем файл с информацией о книгах

    :param file_name: Путь до файла с книгами
    """
    with open(file_name, 'r') as csv_data:
        books = list(csv.DictReader(csv_data))
        CountInfo.COUNT_BOOKS = len(books)

        return [
            {
                'title': book.get('Title'),
                'author': book.get('Author'),
                'pages': book.get('Pages'),
                'genre': book.get('Genre'),
            }
            for book in books
        ]


def create_json(data: list, file_path: str) -> None:
    """
    Формируем json файл c результатами

    :param data: Список пользователе
    :param file_path: Путь для json файла
    """
    with open(file_path, 'w', encoding='utf-8') as jf:
        json.dump(data, jf, indent=3, ensure_ascii=False)
    print(f"Result file '{file_path}' was created!")


def dict_maker(users: list, books: list) -> list:
    """
    Выдаем каждому пользователю книги 'максимально поровну'

    :param users: Список с пользователями
    :param books: Список с книгами
    """
    min_books = 0
    max_books = CountInfo.COUNT_BOOKS // CountInfo.COUNT_USERS
    count_users_with_more_books = CountInfo.COUNT_BOOKS % CountInfo.COUNT_USERS

    for user_id, user in enumerate(users, start=1):
        if user_id <= count_users_with_more_books:
            max_books += 1
        user.get('books').extend(books[min_books: max_books])
        min_books, max_books = max_books, max_books + CountInfo.COUNT_BOOKS // CountInfo.COUNT_USERS
    return users
