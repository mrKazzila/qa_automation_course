from datetime import datetime

from comands import PsAuxParser


def generate_result_file_name() -> str:
    date_format = datetime.now().strftime('%d-%m-%Y-%H:%M')
    return f'{date_format}-scan.txt'


def create_file(file_name: str, result_info) -> None:
    with open(file_name, 'w') as result_file:
        result_file.write(result_info)


class ReportCreator(PsAuxParser):
    """ Клас форматирует данные под репорт. """

    @property
    def get_system_users(self) -> str:
        return ', '.join(self._get_unique_users())

    @property
    def get_count_process(self) -> int:
        return len(self._filter_rows()) - 1

    @property
    def get_users_process(self) -> str:
        return ' '.join([
            f'{user} : {self._get_count_users()[user]},{self.INDENT}'
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
        return f'System users: {self.get_system_users}\n' \
               f'Processes running: {self.get_count_process}\n' \
               f'User processes: {self.INDENT} {self.get_users_process}' \
               f'Total memory used: {self.get_all_cpu_usage} Mb\n' \
               f'Total CPU used: {self.get_all_mem_usage}%\n' \
               f'Uses the most memory: ' \
               f'"{self.biggest_mem_process_name}" - {self.biggest_mem_process_count}Mb\n' \
               f'Most CPU uses: "{self.biggest_cpu_process_name}" - {self.biggest_cpu_process_count}%\n'
