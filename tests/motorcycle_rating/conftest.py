from pymongo import MongoClient
import pytest
from src.adapters.repository.configs import MongoDbRepositoryConfig
from src.entrypoints.payload_models import MotorcycleRatingPayload
from src.motorcycle_rating.domain.models.motorcycle_rating import MotorcycleRating
from src.motorcycle_rating.domain.models.motorcycle_rating_data_from_client import MotorcycleRatingDataFromClient


@pytest.fixture
def motorcycle_rating_data_from_client_message():
    return {
            "mail_user": "foo@bar.com",
            "motorcycle_name": "CB",
            "motorcycle_manufacturer": "HONDA",
            "motorcycle_release_year": "2021",
            "star_rating": 5
    }


@pytest.fixture
def client_payload(motorcycle_rating_data_from_client_message):
    return MotorcycleRatingPayload(
        mail_user=motorcycle_rating_data_from_client_message["mail_user"],
        motorcycle_name=motorcycle_rating_data_from_client_message["motorcycle_name"],
        motorcycle_manufacturer=motorcycle_rating_data_from_client_message["motorcycle_manufacturer"],
        motorcycle_release_year=motorcycle_rating_data_from_client_message["motorcycle_release_year"],
        star_rating=motorcycle_rating_data_from_client_message["star_rating"],
    )


@pytest.fixture
def motorcycle_rating_data_from_client(motorcycle_rating_data_from_client_message):
    return MotorcycleRatingDataFromClient.parse_obj(motorcycle_rating_data_from_client_message)


@pytest.fixture
def motorcycle_rating(motorcycle_rating_data_from_client_message):
    return MotorcycleRating.parse_obj(motorcycle_rating_data_from_client_message)


@pytest.fixture
def mongodb_motorcycle_rating_repository(motorcycle_rating):
    config = MongoDbRepositoryConfig()
    client = MongoClient(config.connection_string)
    motorcycle_db = client[config.database]
    collection_name = motorcycle_db['motorcycle_ratings']
    collection_name.insert_one(motorcycle_rating.dict())
