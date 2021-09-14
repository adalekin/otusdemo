from pydantic import BaseModel


class UserRegistered(BaseModel):
    user_id: int
