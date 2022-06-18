from pydantic import BaseModel


class ClientPayload(BaseModel):
    name: str
    manufacturer: str
    release_year: str
