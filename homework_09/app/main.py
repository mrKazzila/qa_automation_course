#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import functools
import traceback as tb

import helpers as helpers
from FileManager import FileManager


def exception_decorator(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        try:
            f(*args, **kwargs)
        except Exception as e:
            print(f'Error:\n {tb.format_exception(type(e), e, e.__traceback__)}')

    return wrapper


@exception_decorator
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--logs_path', type=str, help='Path with logs', required=True)
    parser.add_argument('-o', '--output_file_path', type=str, help='Output file path', required=False)
    args = parser.parse_args()

    logs_path = args.logs_path
    print(f'Variable for the path to the artifacts folder: {logs_path}')
    FileManager.check_file_exist(file_path=logs_path)

    output_file_path = args.output_file_path or FileManager.create_result_file_name()
    print(f'Variable for the output file: {output_file_path}')
    is_file = helpers.check_is_file(log_path=logs_path)

    log_info = helpers.file_parse(logs_path) if is_file else helpers.parse_dir(logs_path)
    FileManager.writer(output_file_path, log_info)


if __name__ == '__main__':
    main()
