from pydantic import BaseModel


class FavoriteMotorcycleDataFromClient(BaseModel):
    mail_user: str
    motorcycle_name: str
    motorcycle_manufacturer: str
    motorcycle_release_year: str
