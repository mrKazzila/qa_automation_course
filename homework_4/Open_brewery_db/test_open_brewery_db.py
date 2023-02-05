import pytest
import requests

from open_brewery_validators import SingleBreweryValidator


def test_status_code_api(base_url):
    response = requests.get(url=base_url).status_code
    assert response == 200


@pytest.mark.parametrize('by_type', [
    'micro',
    'nano',
    'regional',
    'brewpub',
    'large',
    'planning',
    'bar',
    'contract',
    'closed',
    pytest.param('proprietor', marks=pytest.mark.xfail(reason='Doc bug', strict=True)),
])
def test_status_code_filter_by_type(base_url, by_type):
    result = requests.get(
        url=f'{base_url}/breweries?by_type={by_type}',
    )
    assert result.status_code == 200


def test_validate_brewery(base_url):
    api_json = requests.get(url=f'{base_url}/breweries/madtree-brewing-cincinnati').text
    assert SingleBreweryValidator.parse_raw(api_json)


@pytest.mark.xfail(reason='Doc bug', strict=True)
def test_max_autocomplete_returned(base_url):
    result = requests.get(
        url=f'{base_url}/breweries/autocomplete?query=dog',
    ).json()
    assert len(result) <= 15


@pytest.mark.parametrize('city', ['San Diego', 'Alameda'])
def test_filter_by_city(base_url, city):
    result = requests.get(
        url=f'{base_url}/breweries?by_city={city.replace(" ", "_").lower()}',
    ).json()
    for brewery in result:
        assert brewery.get('city') == city
