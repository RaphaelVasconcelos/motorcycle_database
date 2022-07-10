class FakeFavoriteMotorcycleRepository():
    def __init__(self, empty: bool = False):
        self.empty = empty

    def get_favorite_motorcycle_list(self, favorite_motorcycle):
        if self.empty:
            return []
        return ["CB"]
