from src.models.user import User


def build_user(**kwargs):
    return User.parse_obj(kwargs)
