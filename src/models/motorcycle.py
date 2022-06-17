from pydantic import BaseModel


class Motorcycle(BaseModel):
    name: str
    manufacturer: str
    release_year: str
