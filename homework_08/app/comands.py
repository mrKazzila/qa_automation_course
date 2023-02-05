from collections import Counter
from subprocess import run

PS_AUX = run(['ps', 'aux'], capture_output=True)


class PsAuxParser:
    INDENT = '\n''\t'

    @staticmethod
    def _get_data_from_stdout() -> str:
        return str(PS_AUX.stdout)[2:-3]

    def _get_rows(self) -> list:
        return self._get_data_from_stdout().split(r'\n')

    def _get_filtered_rows(self) -> list:
        return [list(filter(None, row.split(' '))) for row in self._get_rows()]

    def _filter_rows(self) -> list:
        return [row[:10] + [' '.join(row[10:])] for row in self._get_filtered_rows()]

    def _get_users(self) -> list:
        return [row[0] for row in self._filter_rows()[1:]]

    def _get_count_users(self) -> Counter:
        return Counter(self._get_users())

    def _sort_users(self) -> list:
        return sorted(self._get_users(), key=lambda x: -self._get_count_users()[x])

    def _get_unique_users(self) -> list:
        unique_users = []
        for user in self._sort_users():
            if user not in unique_users:
                unique_users.append(user)
        return unique_users

    def _get_process_names(self) -> list:
        return [row[-1] for row in self._filter_rows()[1:]]

    def _cpu_usages_info(self) -> list:
        return [float(row[2]) for row in self._filter_rows()[1:]]

    def _mem_usages_info(self) -> list:
        return [float(row[5]) / 1024 for row in self._filter_rows()[1:]]

    def _get_max_cpu_data(self) -> int:
        cpu = self._cpu_usages_info()
        return cpu.index(max(cpu))

    def _get_max_memory_data(self) -> int:
        mem = self._mem_usages_info()
        return mem.index(max(mem))
