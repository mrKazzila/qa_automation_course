from pydantic import BaseModel, root_validator


class SinglePostValidator(BaseModel):
    id: int  # noqa A003
    title: str
    body: str
    userId: int  # noqa N815


class TestSchemaValidator(BaseModel):
    id: int  # noqa A003
    title: str
    body: str
    userId: int  # noqa N815

    @root_validator
    def check_test_post_response(self, values):
        values_list = [1, 'foo', 'bar', 101]
        for value in values.values():
            if value not in values_list:
                raise ValueError('Not correct data')
            return values
