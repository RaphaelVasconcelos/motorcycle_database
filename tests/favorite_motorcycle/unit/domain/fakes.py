class FakeFavoriteMotorcycleRepository():
    def __init__(self, empty: bool = False):
        self.empty = empty

    def get_favorite_motorcycles(self, favorite_motorcycle):
        if self.empty:
            return []
        return ["CB"]
