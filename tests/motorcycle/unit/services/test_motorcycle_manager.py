import pytest
from src.models.motorcycle.data_from_client import DataFromClient
from src.services.motorcycle.motorcycle_manager import (
    get_motorcyle,
    motorcyle_list,
    process_new_motorcyle,
    remove_motorcyle,
    update_motorcyle,
)


def test_it_should_persist_new_motorcycle(data_from_client):
    motorcycle_was_add = process_new_motorcyle(data_from_client)

    assert motorcycle_was_add is True


@pytest.mark.usefixtures('mongodb_repository')
def test_it_should_remove_motorcycle(data_from_client):
    motorcycle_was_removed = remove_motorcyle(data_from_client)

    assert motorcycle_was_removed is True


@pytest.mark.usefixtures('mongodb_repository')
def test_it_should_update_motorcycle(data_from_client):
    motorcycle_to_update = DataFromClient.parse_obj(data_from_client.dict())
    motorcycle_to_update.release_year = "2022"

    motorcycle_was_updated = update_motorcyle(motorcycle_to_update)
    assert motorcycle_was_updated is True


@pytest.mark.usefixtures('mongodb_repository')
def test_it_should_get_motorcycle(data_from_client, motorcycle):
    returned_motorcycle = get_motorcyle(motorcycle)

    assert returned_motorcycle.name == data_from_client.name
    assert returned_motorcycle.manufacturer == data_from_client.manufacturer
    assert returned_motorcycle.release_year == data_from_client.release_year


@pytest.mark.usefixtures('mongodb_repository')
def test_it_should_list_motorcycles(data_from_client):
    returned_motorcycle_list = motorcyle_list()
    first_motorcycle = returned_motorcycle_list[0]

    assert len(returned_motorcycle_list) == 1
    assert first_motorcycle["name"] == data_from_client.name
    assert first_motorcycle["manufacturer"] == data_from_client.manufacturer
    assert first_motorcycle["release_year"] == data_from_client.release_year
