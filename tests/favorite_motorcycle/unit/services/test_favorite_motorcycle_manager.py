import pytest

from src.favorite_motorcycles.services.favorite_motorcycle_manager import toggle_favorite_motorcyle


@pytest.mark.usefixtures('mongodb_user_repository')
def test_it_should_add_a_favorite_motorcycle(favorite_motorcycle_data_from_client):
    toggle_result = toggle_favorite_motorcyle(favorite_motorcycle_data_from_client)

    assert toggle_result.action == "add"
    assert toggle_result.is_succeed is True


@pytest.mark.usefixtures('mongodb_user_repository')
def test_it_should_remove_favorite_motorcycle(favorite_motorcycle_data_from_client):
    toggle_favorite_motorcyle(favorite_motorcycle_data_from_client)
    toggle_result = toggle_favorite_motorcyle(favorite_motorcycle_data_from_client)

    assert toggle_result.action == "remove"
    assert toggle_result.is_succeed is True
