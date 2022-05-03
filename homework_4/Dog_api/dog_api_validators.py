from pydantic import BaseModel


class AllBreedsValidator(BaseModel):
    message: dict
    status: str


class RandomDogImageValidator(BaseModel):
    message: str
    status: str
