from src.services.process_new_motorcycle import process_new_motorcyle


def test_it_should_persist_new_motorcycle(data_from_client):
    motorcycle_added = process_new_motorcyle(data_from_client)

    assert motorcycle_added.name == data_from_client.name
    assert motorcycle_added.manufacturer == data_from_client.manufacturer
    assert motorcycle_added.release_year == data_from_client.release_year
