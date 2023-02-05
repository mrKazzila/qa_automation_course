import pytest
import requests
from jsonplaceholder_validators import SinglePostValidator, TestSchemaValidator


def test_status_code_api(base_url):
    response = requests.get(url=base_url)
    assert response.status_code == 200


@pytest.mark.parametrize('routes', [
    '/posts/1/comments',
    '/albums/1/photos',
    '/users/1/albums',
    '/users/1/todos',
    '/users/1/posts',
])
def test_nested_data(base_url, routes):
    response = requests.get(url=f'{base_url}{routes}')
    assert response.status_code == 200


def test_delete_posts(base_url):
    response = requests.delete(url=f'{base_url}/posts/1')
    assert response.status_code == 200
    assert response.json() == {}


def test_validate_single_post(base_url):
    response = requests.get(url=f'{base_url}/posts/1').text
    assert SinglePostValidator.parse_raw(response)


def test_create_resource(base_url, header, post_data):
    response = requests.post(
        url=f'{base_url}/posts',
        headers=header,
        json=post_data,
    )
    assert TestSchemaValidator.parse_raw(response.text)


@pytest.mark.parametrize('start_routes, end_routes, expected_count', [
    ('/posts/', '/comments', 5),
    ('/albums/', '/photos', 50),
    ('/users/', '/albums', 10),
    ('/users/', '/todos', 20),
    ('/users/', '/posts', 10),
])
def test_users_nested(base_url, start_routes, end_routes, expected_count):
    for page_id in range(1, 11):
        response = requests.get(
            url=f'{base_url}{start_routes}{page_id}{end_routes}',
        ).json()
        assert len(response) == expected_count
