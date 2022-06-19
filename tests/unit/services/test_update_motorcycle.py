from src.models.data_from_client import DataFromClient
from src.services.process_new_motorcycle import process_new_motorcyle
from src.services.update_motorcycle import update_motorcyle


def test_it_should_update_motorcycle(data_from_client):
    process_new_motorcyle(data_from_client)
    motorcycle_to_update = DataFromClient.parse_obj(data_from_client.dict())
    motorcycle_to_update.release_year = "2022"

    updated_motorcycle = update_motorcyle(motorcycle_to_update)

    assert updated_motorcycle.name == motorcycle_to_update.name
    assert updated_motorcycle.manufacturer == motorcycle_to_update.manufacturer
    assert updated_motorcycle.release_year == motorcycle_to_update.release_year
