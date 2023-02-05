from typing import Union

from pydantic import BaseModel


class SingleBreweryValidator(BaseModel):
    id: str  # noqa A003
    brewery_type: str
    name: str
    street: Union[None, str]
    address_2: Union[None, str]
    address_3: Union[None, str]
    city: str
    state: str
    county_province: Union[None, str]
    postal_code: Union[None, str]
    country: str
    longitude: Union[None, str]
    latitude: Union[None, str]
    phone: str
    website_url: str
    updated_at: str
    created_at: str
