from src.models.motorcycle.data_from_client import DataFromClient


def build_data_from_client(**kwargs):
    return DataFromClient.parse_obj(kwargs)
