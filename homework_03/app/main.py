#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import traceback as tb
from functools import wraps

from helpers import (create_json, dict_maker, read_data_with_books,
                     read_data_with_users)
from settings import (DEFAULT_PATH_BOOKS_FILE, DEFAULT_PATH_RESULT_FILE,
                      DEFAULT_PATH_USERS_FILE)


def exception_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            print('Start')
            func(*args, **kwargs)
            print('Done!')
        except Exception as error:
            trace = tb.format_exception(type(error), error, error.__traceback__)
            print('\n'.join(trace))

    return wrapper


@exception_decorator
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--users_file_path', type=str, help='Users file path', required=False)
    parser.add_argument('-b', '--books_file_path', type=str, help='Books file path', required=False)
    parser.add_argument('-r', '--result_file_path', type=str, help='Result file path', required=False)
    args = parser.parse_args()

    file_with_users = args.users_file_path or DEFAULT_PATH_USERS_FILE
    file_with_books = args.books_file_path or DEFAULT_PATH_BOOKS_FILE
    result_file_path = args.result_file_path or DEFAULT_PATH_RESULT_FILE

    users = read_data_with_users(file_name=file_with_users)
    books = read_data_with_books(file_name=file_with_books)

    result = dict_maker(
        users=users,
        books=books,
    )

    create_json(
        data=result,
        file_path=result_file_path,
    )


if __name__ == '__main__':
    main()
