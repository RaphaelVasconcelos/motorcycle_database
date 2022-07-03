import pytest
from src.models.user.user_data_from_client import UserDataFromClient
from src.services.users.user_manager import process_new_user, update_user


def test_it_should_persist_new_user(user_data_from_client):
    user_was_add = process_new_user(user_data_from_client)

    assert user_was_add is True


@pytest.mark.usefixtures('mongodb_user_repository')
def test_it_should_update_user(user_data_from_client):
    user_to_update = UserDataFromClient.parse_obj(user_data_from_client.dict())
    user_to_update.age = "32"

    motorcycle_was_updated = update_user(user_to_update)
    assert motorcycle_was_updated is True
