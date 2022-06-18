from fastapi import FastAPI

from src.entrypoints.router import add_routes


def create_app():
    app = FastAPI()
    add_routes(app)
    return app
