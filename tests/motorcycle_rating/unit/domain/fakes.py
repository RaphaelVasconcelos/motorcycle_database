class FakeMotorcycleRatingRepository():
    def __init__(self, empty: bool = False):
        self.empty = empty

    def get_motorcycle_rating_by_user(self, favorite_motorcycle):
        if self.empty:
            return {}
        return {
            "mail_user": "foo@bar.com",
            "motorcycle_name": "CB",
            "motorcycle_manufacturer": "HONDA",
            "motorcycle_release_year": "2021",
            "star_rating": 5
        }
