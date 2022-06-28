from src.factories.user_data_from_client import build_user_data_from_client


def test_it_should_build_data_from_client_object(user_data_from_client):
    built_data_from_client = build_user_data_from_client(
        name=user_data_from_client.name,
        mail=user_data_from_client.mail,
        age=user_data_from_client.age
    )

    assert built_data_from_client == user_data_from_client
