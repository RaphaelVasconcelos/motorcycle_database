from src.adapters.repository.list_repository import MotorcycleListRepository
from src.models.motorcycle import Motorcycle


def test_it_should_add_motorcycle_to_list(motorcycle):
    list_repository = MotorcycleListRepository()
    list_repository.add(motorcycle)

    first_motorcycle = list_repository._collection[0]

    assert len(list_repository._collection) == 1
    assert first_motorcycle.name == motorcycle.name
    assert first_motorcycle.manufacturer == motorcycle.manufacturer
    assert first_motorcycle.release_year == motorcycle.release_year


def test_it_should_update_motorcycle(motorcycle):
    list_repository = MotorcycleListRepository()
    list_repository.add(motorcycle)

    updated_motorcycle = Motorcycle.parse_obj(motorcycle.dict())
    updated_motorcycle.release_year = "2022"
    list_repository.update(updated_motorcycle)

    first_motorcycle = list_repository._collection[0]

    assert len(list_repository._collection) == 1
    assert first_motorcycle.name == updated_motorcycle.name
    assert first_motorcycle.manufacturer == updated_motorcycle.manufacturer
    assert first_motorcycle.release_year == updated_motorcycle.release_year


def test_it_should_remove_motorcycle(motorcycle):
    list_repository = MotorcycleListRepository()
    list_repository.add(motorcycle)

    list_repository.remove(motorcycle)

    assert len(list_repository._collection) == 0


def test_it_should_get_motorcycle(motorcycle):
    list_repository = MotorcycleListRepository()
    list_repository.add(motorcycle)

    returned_motorcyle = list_repository.get(motorcycle)

    assert returned_motorcyle.name == motorcycle.name
    assert returned_motorcyle.manufacturer == motorcycle.manufacturer
    assert returned_motorcyle.release_year == motorcycle.release_year


def test_it_should_return_a_list_of_motorcycles(motorcycle):
    list_repository = MotorcycleListRepository()
    list_repository.add(motorcycle)

    motorcyle_list = list_repository.motorcycle_list()
    first_motorcycle = motorcyle_list[0]

    assert len(motorcyle_list) == 1
    assert first_motorcycle.name == motorcycle.name
    assert first_motorcycle.manufacturer == motorcycle.manufacturer
    assert first_motorcycle.release_year == motorcycle.release_year
