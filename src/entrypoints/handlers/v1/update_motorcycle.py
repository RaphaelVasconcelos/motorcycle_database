from fastapi import Response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from src.entrypoints.payload_models import ClientPayload
from src.factories.data_from_client import build_data_from_client
from src.services.motorcycle_manager import update_motorcyle


def handle_update_motorcycle(client_payload: ClientPayload) -> Response:
    data_from_client = build_data_from_client(**client_payload.dict())
    result = update_motorcyle(data_from_client)

    return JSONResponse(jsonable_encoder(result))
