from fastapi import FastAPI

from src.examle_app.routes import router as example_router


def create_app() -> FastAPI:
    _app = FastAPI()
    _app.include_router(example_router, prefix="/api/example")
    return _app
