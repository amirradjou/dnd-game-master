from fastapi import FastAPI
from app.routes import game

app = FastAPI()

app.include_router(game.router)

