from pydantic import BaseModel, validator


class GetUserByUsernameResponse(BaseModel):
    id: int
    username: str
    firstName: str
    lastName: str
    email: str
    password: str
    phone: str
    userStatus: int

    @validator('id')
    def id_should_be_int(cls, v: int) -> int:
        if type(v) != int:
            raise ValueError('id is not int')
        return v

    @validator('username')
    def username_should_be_str(cls, v: str) -> str:
        if type(v) != str:
            raise ValueError('username is not str')
        return v

    @validator('firstName')
    def firstname_should_be_str(cls, v: str) -> str:
        if type(v) != str:
            raise ValueError('firstName is not str')
        return v

    @validator('lastName')
    def lastname_should_be_str(cls, v: int) -> str:
        if type(v) != str:
            raise ValueError('lastName is not str')
        return v

    @validator('email')
    def email_should_be_str(cls, v: str) -> str:
        if type(v) != str:
            raise ValueError('email is not str')
        return v

    @validator('password')
    def password_should_be_str(cls, v: str) -> str:
        if type(v) != str:
            raise ValueError('password is not str')
        return v

    @validator('phone')
    def phone_should_be_str(cls, v: int) -> str:
        if type(v) != str:
            raise ValueError('phone is not str')
        return v

    @validator('userStatus')
    def user_status_should_be_int(cls, v: str) -> int:
        if type(v) != int:
            raise ValueError('userStatus is not int')
        return v


class GetRemoteUserByUsernameResponse(BaseModel):
    code: int
    type: str
    message: str

    @validator('code')
    def id_should_be_int(cls, v: int) -> int:
        if type(v) != int:
            raise ValueError('code is not int')
        return v

    @validator('type')
    def username_should_be_str(cls, v: str) -> str:
        if type(v) != str:
            raise ValueError('type is not str')
        return v

    @validator('message')
    def firstname_should_be_str(cls, v: str) -> str:
        if type(v) != str:
            raise ValueError('message is not str')
        return v
