import pytest
import requests

from dog_api_validators import (
    AllBreedsValidator,
    RandomDogImageValidator
)


def test_status_code_api(base_url):
    r = requests.get(url=base_url)
    assert r.status_code == 200


def test_image_status_code(base_url):
    result = requests.get(url=f'{base_url}/breeds/image/random/3').json()
    for b in result.get("message"):
        image_code = requests.get(url=b).status_code
        assert image_code == 200


def test_validate_list_all_breeds(base_url):
    api_json = requests.get(url=f'{base_url}/breeds/list/all').text
    assert AllBreedsValidator.parse_raw(api_json)


def test_validate_random_image(base_url):
    api_json = requests.get(url=f'{base_url}/breeds/image/random').text
    assert RandomDogImageValidator.parse_raw(api_json)


def test_max_random_images(base_url):
    api_json = requests.get(url=f'{base_url}/breeds/image/random/51').json()
    assert len(api_json.get("message")) <= 50


@pytest.mark.parametrize('image_count', [1, 3, 4, 6])
def test_count_images(base_url, image_count):
    result = requests.get(url=f'{base_url}/breeds/image/random/{image_count}').json()
    assert len(result.get("message")) == image_count


@pytest.mark.parametrize('breed', ['hound', 'buhund'])
def test_breed_in_images(base_url, breed):
    result = requests.get(url=f'{base_url}/breed/{breed}/images').json()
    for b in result.get("message"):
        assert breed in b
