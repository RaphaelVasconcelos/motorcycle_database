import pytest
from src.favorite_motorcycles.services.favorite_motorcycle_manager import process_new_favorite_motorcyle


@pytest.mark.usefixtures('mongodb_user_repository')
def test_it_should_persist_a_new_favorite_motorcycle(favorite_motorcycle_data_from_client):
    favorite_motorcycle_was_add = process_new_favorite_motorcyle(favorite_motorcycle_data_from_client)

    assert favorite_motorcycle_was_add is True
