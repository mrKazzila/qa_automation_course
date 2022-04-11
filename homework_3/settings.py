from dataclasses import dataclass


@dataclass
class CountInfo:
    """
    Класс для хранения данных о количестве пользователей и книг
    """
    COUNT_USERS: int = 0
    COUNT_BOOKS: int = 0
