import requests
from pydantic import BaseModel, ValidationError, validator


class CreatingUserError(AssertionError):
    """Ошибка создания пользователя"""

    pass


class CreateUserRequest(BaseModel):
    id: int = 0
    username: str
    firstName: str
    lastName: str
    email: str
    password: str
    phone: str
    userStatus: int


class CreateUserResponse(BaseModel):
    code: int
    type: str
    message: str
    # code: str
    # type: int
    # message: int

    @validator('code')
    # def code_should_be_int(cls, v: str) -> str:
    #     if v is not str:
    #         raise ValueError('code is not int')
    #     return v
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


input_json = """
{
  "id": 0,
  "username": "y3ll0w",
  "firstName": "Konstantin",
  "lastName": "Varvarkin",
  "email": "example@gmail.com",
  "password": "!w36fdgdfa",
  "phone": "+79998887654",
  "userStatus": 0
}
"""


class TestCreateUser:
    def test_create_user(self):
        try:
            create_user_request = CreateUserRequest.parse_raw(input_json)
            j = create_user_request.json()
            url = "https://petstore.swagger.io/v2/user"
            payload = j
            headers = {
                'accept': 'application/json',
                'Content-Type': 'application/json'
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            create_user_response_json = response.json()
            if response.status_code != 200:
                raise CreatingUserError
            else:
                try:
                    CreateUserResponse(
                        code=create_user_response_json['code'],
                        type=create_user_response_json['type'],
                        message=create_user_response_json['message']
                    )
                except ValidationError as e:
                    raise e
                return f'"Response body:", {response.text}, "Response code:", {response.status_code}'
        except requests.ConnectionError:
            print("API connection error")
