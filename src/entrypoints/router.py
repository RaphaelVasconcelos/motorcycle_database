from fastapi import FastAPI

from src.entrypoints.handlers.v1.new_motorcycle import handle_new_motorcycle
from src.entrypoints.handlers.v1.remove_motorcycle import handle_remove_motorcycle
from src.entrypoints.handlers.v1.update_motorcycle import handle_update_motorcycle


def add_routes(app: FastAPI):
    # application
    app.add_api_route(
        '/v1/motorcycle/add/',
        handle_new_motorcycle,
        methods=['POST'],
    )

    app.add_api_route(
        '/v1/motorcycle/update/',
        handle_update_motorcycle,
        methods=['POST'],
    )

    app.add_api_route(
        '/v1/motorcycle/remove/',
        handle_remove_motorcycle,
        methods=['POST'],
    )
