from fastapi import FastAPI
from contextlib import asynccontextmanager

from apps import users, auth

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

def create_app():
    app = FastAPI(lifespan=lifespan)

    for api in [users, auth]:
        app.include_router(api.router.router)

    return app

app = create_app()