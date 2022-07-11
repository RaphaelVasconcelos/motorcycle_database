from pydantic import BaseModel


class MotorcycleRating(BaseModel):
    mail_user: str
    motorcycle_name: str
    motorcycle_manufacturer: str
    motorcycle_release_year: str
    star_rating: int
