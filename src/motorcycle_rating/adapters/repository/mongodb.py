from pymongo import MongoClient
from src.adapters.repository.configs import MongoDbRepositoryConfig
from src.motorcycle_rating.adapters.repository.port import MotorcycleRatingRepository
from src.motorcycle_rating.domain.models.motorcycle_rating import MotorcycleRating


class MongoDbMotorcycleRatingRepository(MotorcycleRatingRepository):
    def __init__(self, config: MongoDbRepositoryConfig = MongoDbRepositoryConfig()):
        self._client = MongoClient(config.connection_string)
        self.motorcycle_db = self._client[config.database]

    def add_motorcycle_rating(self, motorcycle_rating: MotorcycleRating):
        collection_name = self.motorcycle_db['motorcycle_ratings']
        result = collection_name.insert_one(motorcycle_rating.dict())
        return result.acknowledged

    def update_motorcycle_rating(self, motorcycle_rating: MotorcycleRating):
        collection_name = self.motorcycle_db['motorcycle_ratings']
        result = collection_name.update_one(
            {'mail_user': motorcycle_rating.mail_user, 'motorcycle_name': motorcycle_rating.motorcycle_name},
            {'$set': {'star_rating': motorcycle_rating.star_rating}}
        )

        return result.modified_count > 0

    def get_motorcycle_rating_by_user(self, motorcycle_rating: MotorcycleRating):
        collection_name = self.motorcycle_db['motorcycle_ratings']
        result = collection_name.find_one(
            {'mail_user': motorcycle_rating.mail_user, 'motorcycle_name': motorcycle_rating.motorcycle_name},
        )
        return result
