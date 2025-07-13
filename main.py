from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager

from router import api_router
from database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host="localhost",
        port=8080
    )
