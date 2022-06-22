from fastapi import Response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from src.entrypoints.payload_models import ClientPayload
from src.services.motorcycle_manager import motorcyle_list


def handle_motorcycle_list(client_payload: ClientPayload) -> Response:
    motorcycles = motorcyle_list()

    return JSONResponse(jsonable_encoder(motorcycles))
