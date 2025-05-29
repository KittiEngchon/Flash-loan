from fastapi import FastAPI
from api.strategies import router as strategies_router

app = FastAPI()

app.include_router(strategies_router, prefix="/api")
