from src.services.process_new_motorcycle import process_new_motorcyle


def test_it_should_persist_new_motorcycle(data_from_client):
    motorcycle_list = process_new_motorcyle(data_from_client)

    assert len(motorcycle_list) == 1
