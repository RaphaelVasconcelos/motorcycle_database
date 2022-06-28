from src.adapters.repository.user.mongodb import MongoDbUserRepository
from src.factories.user import build_user
from src.models.user_data_from_client import UserDataFromClient


def process_new_user(
    data_from_client: UserDataFromClient,
    repository: MongoDbUserRepository = MongoDbUserRepository()
):
    new_user = build_user(**data_from_client.dict())
    return repository.add(new_user)