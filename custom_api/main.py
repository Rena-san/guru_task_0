from http.client import HTTPException

from fastapi import FastAPI
from pydantic import BaseModel
from user_data.user_data import USERS, SUPPORT_INFO

app = FastAPI()


class UserData(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class SupportData(BaseModel):
    url: str
    text: str

class UsersResponseModel(BaseModel):
    data: list[UserData]
    support: SupportData

class ResponseModel(BaseModel):
    data: UserData
    support: SupportData

@app.get("/users", response_model=UsersResponseModel)
def get_users():
    return {
        "data": USERS,
        "support": SUPPORT_INFO
    }



@app.get("/users/{user_id}", response_model=ResponseModel)
def get_user_or_404(user_id: int):
    for user in USERS:
        if user["id"] == user_id:
            return {
                "data": user,
                "support": SUPPORT_INFO
            }
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error": "User not found", "user_id": user_id}
        )
