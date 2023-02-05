import pytest


@pytest.fixture
def base_url():
    return 'https://jsonplaceholder.typicode.com'


@pytest.fixture
def post_data():
    return dict(
        userId=1,
        title='foo',
        body='bar',
    )


@pytest.fixture
def header():
    return {'Content-type': 'application/json; charset=UTF-8'}
