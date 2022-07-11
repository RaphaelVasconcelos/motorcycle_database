import pytest
from src.motorcycle_rating.domain.models.motorcycle_rating_data_from_client import MotorcycleRatingDataFromClient

from src.motorcycle_rating.services.motorcycle_rating_manager import handle_motorcyle_rating


def test_it_should_add_motorcycle_rating(motorcycle_rating_data_from_client):
    rating_result = handle_motorcyle_rating(motorcycle_rating_data_from_client)

    assert rating_result.action == "add"
    assert rating_result.is_succeed is True


@pytest.mark.usefixtures('mongodb_motorcycle_rating_repository')
def test_it_should_remove_favorite_motorcycle(motorcycle_rating_data_from_client):
    updated_rating = MotorcycleRatingDataFromClient.parse_obj(motorcycle_rating_data_from_client.dict())
    updated_rating.star_rating = 3
    rating_result = handle_motorcyle_rating(updated_rating)

    assert rating_result.action == "update"
    assert rating_result.is_succeed is True
