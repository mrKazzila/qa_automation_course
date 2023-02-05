import pytest
import requests


@pytest.fixture
def base_url(request):
    return request.config.getoption('--url')


@pytest.fixture
def status_code(request):
    return int(request.config.getoption('--status_code'))


def test_status_code_for_url(base_url, status_code):
    response = requests.get(url=base_url)
    assert response.status_code == status_code
