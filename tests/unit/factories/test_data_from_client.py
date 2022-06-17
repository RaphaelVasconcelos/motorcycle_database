from src.factories.data_from_client import build_data_from_client


def test_it_should_build_data_from_client_object(data_from_client):
    built_data_from_client = build_data_from_client(
        name=data_from_client.name,
        manufacturer=data_from_client.manufacturer,
        release_year=data_from_client.release_year
    )

    assert built_data_from_client == data_from_client
