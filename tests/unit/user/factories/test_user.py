from src.factories.user.user import build_user


def test_it_should_build_data_from_client_object(user_data_from_client):
    built_user = build_user(
        name=user_data_from_client.name,
        mail=user_data_from_client.mail,
        age=user_data_from_client.age
    )

    assert built_user == user_data_from_client
