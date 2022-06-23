from pydantic import BaseModel


class Motorcycle(BaseModel):
    name: str
    manufacturer: str
    release_year: str

    def __eq__(self, other):
        return (
            other.name == self.name and
            other.manufacturer == self.manufacturer and
            other.release_year == self.release_year
        )
