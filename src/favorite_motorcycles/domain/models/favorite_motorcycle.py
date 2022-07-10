from pydantic import BaseModel


class FavoriteMotorcycle(BaseModel):
    mail_user: str
    motorycle_name: str
    motorycle_manufacturer: str
    motorycle_release_year: str
