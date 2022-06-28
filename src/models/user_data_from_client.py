from pydantic import BaseModel


class UserDataFromClient(BaseModel):
    name: str
    mail: str
    age: str
