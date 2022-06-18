from fastapi import FastAPI

from src.entrypoints.handlers.v1.new_motorcycle import handle_new_motorcycle


def add_routes(app: FastAPI):
    # application
    app.add_api_route(
        '/v1/motorcycle/add/',
        handle_new_motorcycle,
        methods=['POST'],
    )
