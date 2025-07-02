from fastapi import FastAPI
from contextlib import asynccontextmanager

from apps import users

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

def create_app():
    app = FastAPI(lifespan=lifespan)

    for api in [users]:
        app.include_router(api.router.router)
    app.include_router(users.auth.router)

    return app

app = create_app()