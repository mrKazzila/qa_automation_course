import re
from collections import Counter
from typing import Optional, Union

from FileManager import FileManager
from data import Data, methods


def check_is_file(log_path: str) -> bool:
    return True if log_path.endswith('.log') else False


def result_creator(data_count: dict, method_count: dict,
                   popular_ip: dict, longest_requests: dict) -> dict:
    return {
        **data_count,
        **method_count,
        **popular_ip,
        **longest_requests,
    }


def parse_dir(log_file: str) -> dict:
    result = {}
    for path, file_name in FileManager.get_path_with_log_files(log_file):
        result.update({file_name: file_parse(path)})
    return result


def file_parse(log_file: str) -> dict:
    parse_data = {
        line_id: parse_line(line)
        for line_id, line in enumerate(FileManager.parse_log_file(log_file), start=1)
    }
    return result_creator(
        data_count=dict(count=len(parse_data)),
        method_count=get_method_count(data=parse_data),
        popular_ip=get_ip_count(data=parse_data),
        longest_requests=get_longest_requests(data=parse_data),
    )


def parse_line(line: str) -> Data:
    regex_method = re.compile(r'(POST|GET|PUT|DELETE|HEAD|CONNECT|OPTIONS|TRACE|PATCH)')
    regex_ip_address = re.compile(r'(\d{1,3}\.){3}\d{1,3}')
    regex_url = re.compile(r'"(http[s]?:\/\/.+)" "')
    regex_date_time = re.compile(r'\[(.+) \+\d{4}\]')
    regex_duration = re.compile(r'\d+$')

    return Data(
        method_=get_method_match(line=line, regex_=regex_method),
        ip_=get_ip_address_match(line=line, regex_=regex_ip_address),
        url_=get_url_match(line=line, regex_=regex_url),
        date_time_=get_time_match(line=line, regex_=regex_date_time),
        duration_=duration_match(line=line, regex_=regex_duration),
    )


def get_method_match(line: str, regex_: re) -> str:
    match = regex_.search(line)
    return match.group(0) if match else '-'


def get_ip_address_match(line: str, regex_: re) -> str:
    match = regex_.search(line)
    return match.group(0) if match else '-'


def get_url_match(line: str, regex_: re) -> str:
    match = regex_.search(line)
    return match.group(1) if match else '-'


def duration_match(line: str, regex_: re) -> Optional[Union[int, str]]:
    match = regex_.search(line)
    return int(match.group(0)) if match else '-'


def get_time_match(line: str, regex_: re) -> str:
    match = regex_.search(line)
    return match.group(1) if match else '-'


def get_method_count(data: dict) -> dict:
    for info in data.values():
        methods[info.method_] = methods.get(info.method_) + 1
    return {"methods": methods}


def get_ip_count(data: dict, top_: int = 3) -> dict:
    ip_s = Counter([info.ip_ for info in data.values()])
    return {f"top_{top_}_ipS": sorted(ip_s.items(), key=lambda x: -x[1])[:top_]}


def get_longest_requests(data: dict, top_: int = 10) -> dict:
    return {f"top_{top_}_duration": sorted(data.values(), key=lambda x: -x.duration_)[:top_]}
