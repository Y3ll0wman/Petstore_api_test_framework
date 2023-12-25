import json

from typing import List
from pydantic import BaseModel, validator
from utils.RandomData import RandomData


class UserData(BaseModel):
    id: int
    username: str
    firstName: str
    lastName: str
    email: str
    password: str
    phone: str
    userStatus: int


class CreateUserWithInputListRequest(BaseModel):
    __root__: List[UserData]


class CreateUserWithInputListResponse(BaseModel):
    code: int
    type: str
    message: str

    @validator('code')
    def code_should_be_int(cls, v: int) -> int:
        if type(v) != int:
            raise ValueError('code is not int')
        return v

    @validator('type')
    def type_should_be_str(cls, v: str) -> str:
        if type(v) != str:
            raise ValueError('type is not str')
        return v

    @validator('message')
    def message_should_be_str(cls, v: str) -> str:
        if type(v) != str:
            raise ValueError('message is not str')
        return v


input_json = json.dumps(
[
    {
        "id": RandomData.user_id(),
        "username": RandomData.username(),
        "firstName": RandomData.first_name(),
        "lastName": RandomData.last_name(),
        "email": RandomData.email(),
        "password": RandomData.password(),
        "phone": RandomData.phone(),
        "userStatus": 0
    },
    {
        "id": RandomData.user_id(),
        "username": RandomData.username(),
        "firstName": RandomData.first_name(),
        "lastName": RandomData.last_name(),
        "email": RandomData.email(),
        "password": RandomData.password(),
        "phone": RandomData.phone(),
        "userStatus": 0
    }
]
)
