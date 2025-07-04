from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from contextlib import asynccontextmanager

from apps import users, auth

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

def create_app():
    app = FastAPI(lifespan=lifespan)

    for api in [users, auth]:
        app.include_router(api.router.router)

    app.mount("/media/images", StaticFiles(directory="media/images"), name="images")

    return app

app = create_app()