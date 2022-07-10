from src.favorite_motorcycles.domain.services import action_for_this_favorite_motorcycle
from tests.favorite_motorcycle.unit.domain.fakes import FakeFavoriteMotorcycleRepository


def test_it_should_add_favorite_motorcycle(favorite_motorcycle):
    repository = FakeFavoriteMotorcycleRepository(empty=True)
    action_needed = action_for_this_favorite_motorcycle(
        favorite_motorcycle=favorite_motorcycle,
        repository=repository
    )

    assert action_needed == "add"


def test_it_should_remove_favorite_motorcycle(favorite_motorcycle):
    repository = FakeFavoriteMotorcycleRepository()
    action_needed = action_for_this_favorite_motorcycle(
        favorite_motorcycle=favorite_motorcycle,
        repository=repository
    )

    assert action_needed == "remove"
