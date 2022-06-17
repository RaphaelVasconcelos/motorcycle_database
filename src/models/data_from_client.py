from pydantic import BaseModel


class DataFromClient(BaseModel):
    name: str
    manufacturer: str
    release_year: str
