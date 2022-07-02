from src.models.user.user_data_from_client import UserDataFromClient


def build_user_data_from_client(**kwargs):
    return UserDataFromClient.parse_obj(kwargs)
