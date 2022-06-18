from fastapi import Response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from src.entrypoints.payload_models import ClientPayload
from src.factories.data_from_client import build_data_from_client
from src.services.process_new_motorcycle import process_new_motorcyle


def handle_new_motorcycle(client_payload: ClientPayload) -> Response:
    data_from_client = build_data_from_client(**client_payload.dict())
    motorcycle = process_new_motorcyle(data_from_client)

    return JSONResponse(jsonable_encoder(motorcycle))
