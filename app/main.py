from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from api.routes import router
from config.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("server started successfully.")
    yield


app = FastAPI(
    title=settings.APP_NAME,
    lifespan=lifespan,
)

app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=settings.HOST,
        port=settings.PORT,
    )
