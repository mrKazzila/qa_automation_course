from functools import wraps

from homework_3.helpers import *


def exception_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(e)

    return wrapper


@exception_decorator
def main():
    file_with_users = "data/users.json"
    file_with_books = "data/books.csv"

    users = read_data_with_users(file_name=file_with_users)
    books = read_data_with_books(file_name=file_with_books)

    result = dict_maker(
        users=users,
        books=books
    )

    create_json(
        result,
        'result.json'
    )


if __name__ == "__main__":
    main()
