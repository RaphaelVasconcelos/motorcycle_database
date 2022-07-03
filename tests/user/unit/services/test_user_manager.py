import pytest
from src.models.user.user_data_from_client import UserDataFromClient
from src.services.users.user_manager import get_user, process_new_user, remove_user, update_user, user_list


def test_it_should_persist_new_user(user_data_from_client):
    user_was_add = process_new_user(user_data_from_client)

    assert user_was_add is True


@pytest.mark.usefixtures('mongodb_user_repository')
def test_it_should_update_user(user_data_from_client):
    user_to_update = UserDataFromClient.parse_obj(user_data_from_client.dict())
    user_to_update.age = "32"

    user_was_updated = update_user(user_to_update)
    assert user_was_updated is True


@pytest.mark.usefixtures('mongodb_user_repository')
def test_it_should_remove_user(user_data_from_client):
    user_was_removed = remove_user(user_data_from_client)

    assert user_was_removed is True


@pytest.mark.usefixtures('mongodb_user_repository')
def test_it_should_get_user(user_data_from_client, user):
    returned_user = get_user(user)

    assert returned_user["name"] == user_data_from_client.name
    assert returned_user["mail"] == user_data_from_client.mail
    assert returned_user["age"] == user_data_from_client.age


@pytest.mark.usefixtures('mongodb_user_repository')
def test_it_should_list_motorcycles(user_data_from_client):
    returned_user_list = user_list()
    first_user = returned_user_list[0]

    assert len(returned_user_list) == 1
    assert first_user["name"] == user_data_from_client.name
    assert first_user["mail"] == user_data_from_client.mail
    assert first_user["age"] == user_data_from_client.age
