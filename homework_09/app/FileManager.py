import json
import os
from datetime import datetime
from typing import NoReturn, Tuple


class FileManager:

    @staticmethod
    def check_file_exist(file_path: str) -> NoReturn:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f'File or dir {file_path} not found!')

    @staticmethod
    def get_path_with_log_files(path: str) -> Tuple[str, str]:
        for root, _dirs, files in os.walk(path, topdown=False):
            for name in files:
                if name.endswith('.log'):
                    yield os.path.normpath(os.path.join(root, name)), name

    @staticmethod
    def parse_log_file(log_file: str) -> str:
        print(f'Work with file: {log_file}')
        with open(log_file, 'r') as log_f:
            for line in log_f:
                yield line.replace('\n', '').strip()

    @staticmethod
    def create_result_file_name() -> str:
        date_format = datetime.now().strftime('%d-%m-%Y-%H-%M')
        return os.path.join(os.getcwd(), f'parse_result_{date_format}.json')

    @staticmethod
    def writer(output_file: str, log_data) -> None:
        with open(output_file, 'w', encoding='utf-8') as json_file:
            print(json.dumps(log_data, indent=3, ensure_ascii=False))
            json.dump(log_data, json_file, indent=3, ensure_ascii=False)
        print(f'The json file was created, the path for the file: {output_file}')
