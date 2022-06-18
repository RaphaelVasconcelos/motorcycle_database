from src.adapters.repository.list_repository import MotorcycleListRepository


def test_it_should_add_to_list(motorcycle):
    list_repository = MotorcycleListRepository()
    list_repository.add(motorcycle)
    list_repository.add(motorcycle)

    assert len(list_repository._collection) == 2
