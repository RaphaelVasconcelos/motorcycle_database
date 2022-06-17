from src.models.motorcycle import Motorcycle


def build_motorcycle(**kwargs):
    return Motorcycle.parse_obj(kwargs)
