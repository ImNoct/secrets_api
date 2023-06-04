from fastapi import FastAPI
from .routers import generate, secrets
from .database import engine
from .config import config
from . import models
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(generate.router)
app.include_router(secrets.router)


@app.get("/")
async def root():
    return {"message" : "OK"}
