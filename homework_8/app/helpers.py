from datetime import datetime
from typing import NoReturn

from homework_8.app.comands import PsAuxParser


def generate_result_file_name() -> str:
    date_format = datetime.now().strftime("%d-%m-%Y-%H:%M")
    return f'{date_format}-scan.txt'


def create_file(file_name: str, result_info) -> NoReturn:
    with open(file_name, "w") as result_file:
        result_file.write(result_info)


class ReportCreator(PsAuxParser):
    """ Клас форматирует данные под репорт. """

    @property
    def get_system_users(self) -> str:
        return ", ".join(self._get_unique_users())

    @property
    def get_count_process(self) -> int:
        return len(self._filter_rows()) - 1

    @property
    def get_users_process(self) -> str:
        return " ".join([
            f"{user} : {self._get_count_users()[user]},{self.INDENT}"
            for user in self._get_unique_users()
        ])

    @property
    def get_all_cpu_usage(self) -> float:
        return round(sum(self._cpu_usages_info()), 2)

    @property
    def get_all_mem_usage(self) -> float:
        return round(sum(self._mem_usages_info()), 2)

    @property
    def biggest_mem_process_name(self) -> str:
        return self._get_process_names()[self._get_max_memory_data()][:20]

    @property
    def biggest_mem_process_count(self) -> float:
        return round(self._mem_usages_info()[self._get_max_memory_data()], 2)

    @property
    def biggest_cpu_process_name(self) -> str:
        return self._get_process_names()[self._get_max_cpu_data()][:20]

    @property
    def biggest_cpu_process_count(self) -> float:
        return round(self._cpu_usages_info()[self._get_max_cpu_data()], 2)

    def report(self) -> str:
        return f"""Пользователи системы: {self.get_system_users}
Процессов запущено: {self.get_count_process}
Пользовательских процессов: {self.INDENT} {self.get_users_process}
Всего памяти используется: {self.get_all_cpu_usage} Mb
Всего CPU используется: {self.get_all_mem_usage}%
Больше всего памяти использует: '{self.biggest_mem_process_name}' - {self.biggest_mem_process_count}Mb
Больше всего CPU использует: '{self.biggest_cpu_process_name}' - {self.biggest_cpu_process_count}% 
"""
