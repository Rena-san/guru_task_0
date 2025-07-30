from pydantic import BaseModel

from user_data.user_data import USER_DATA_REQRES


class User(BaseModel):
    password: str = None
    email: str = None


def get_user():
    return User(**USER_DATA_REQRES)