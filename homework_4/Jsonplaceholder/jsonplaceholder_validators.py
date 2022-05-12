from pydantic import BaseModel, root_validator


class SinglePostValidator(BaseModel):
    id: int
    title: str
    body: str
    userId: int


class TestSchemaValidator(BaseModel):
    id: int
    title: str
    body: str
    userId: int

    @root_validator
    def check_test_post_response(cls, values):
        values_list = [1, 'foo', 'bar', 101]
        for value in values.values():
            if value not in values_list:
                raise ValueError("Not correct data")
            return values
