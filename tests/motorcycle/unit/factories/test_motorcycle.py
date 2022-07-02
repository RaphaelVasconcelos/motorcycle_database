from src.factories.motorcycle.motorcycle import build_motorcycle


def test_it_should_build_data_from_client_object(data_from_client):
    built_motorcycle = build_motorcycle(
        name=data_from_client.name,
        manufacturer=data_from_client.manufacturer,
        release_year=data_from_client.release_year
    )

    assert built_motorcycle == data_from_client
