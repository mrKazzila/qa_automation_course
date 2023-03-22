import traceback as tb
from functools import wraps

from helpers import ReportCreator, create_file, generate_result_file_name


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
    result = ReportCreator().report()
    create_file(
        file_name=generate_result_file_name(),
        result_info=result,
    )
    print(result)


if __name__ == '__main__':
    main()
