from functools import wraps

from homework_8.app.helpers import ReportCreator, create_file, generate_result_file_name


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
    create_file(
        file_name=generate_result_file_name(),
        result_info=ReportCreator().report()
    )


if __name__ == "__main__":
    main()
