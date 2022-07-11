from src.motorcycle_rating.domain.services import action_for_rating_motorcycle
from tests.motorcycle_rating.unit.domain.fakes import FakeMotorcycleRatingRepository


def test_it_should_add_motorcycle_rating(motorcycle_rating):
    repository = FakeMotorcycleRatingRepository(empty=True)
    action_needed = action_for_rating_motorcycle(
        motorcycle_rating=motorcycle_rating,
        repository=repository
    )

    assert action_needed == "add"


def test_it_should_update_motorcycle_rating(motorcycle_rating):
    repository = FakeMotorcycleRatingRepository()
    action_needed = action_for_rating_motorcycle(
        motorcycle_rating=motorcycle_rating,
        repository=repository
    )

    assert action_needed == "update"
