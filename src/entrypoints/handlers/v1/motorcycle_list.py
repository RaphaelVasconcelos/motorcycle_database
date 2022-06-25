import json
from fastapi import Response
from bson.json_util import dumps
from fastapi.responses import JSONResponse
from src.entrypoints.payload_models import ClientPayload
from src.services.motorcycle_manager import motorcyle_list


def handle_motorcycle_list(client_payload: ClientPayload) -> Response:
    motorcycles = motorcyle_list()

    return JSONResponse(json.loads(dumps(motorcycles)))
