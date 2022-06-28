from src.services.users.user_manager import process_new_user


def test_it_should_persist_new_user(user_data_from_client):
    motorcycle_was_add = process_new_user(user_data_from_client)

    assert motorcycle_was_add is True
