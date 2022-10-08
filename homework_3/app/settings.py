from dataclasses import dataclass


DEFAULT_PATH_USERS_FILE: str = "../data/users.json"
DEFAULT_PATH_BOOKS_FILE: str = "../data/books.csv"
DEFAULT_PATH_RESULT_FILE: str = "../result.json"


@dataclass
class CountInfo:
    """
    Класс для хранения данных о количестве пользователей и книг
    """
    COUNT_USERS: int = 0
    COUNT_BOOKS: int = 0
