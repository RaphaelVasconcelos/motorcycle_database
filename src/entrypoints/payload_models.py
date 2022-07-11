from pydantic import BaseModel


class ClientPayload(BaseModel):
    name: str
    manufacturer: str
    release_year: str


class ClientUserPayload(BaseModel):
    name: str
    mail: str
    age: str


class FavoriteMotorcyclePayload(BaseModel):
    mail_user: str
    motorcycle_name: str
    motorcycle_manufacturer: str
    motorcycle_release_year: str


class MotorcycleRatingPayload(BaseModel):
    mail_user: str
    motorcycle_name: str
    motorcycle_manufacturer: str
    motorcycle_release_year: str
    star_rating: int
