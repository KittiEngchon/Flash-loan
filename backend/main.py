from fastapi import FastAPI
from api.routes import router as strategies_router

app = FastAPI()

app.include_router(strategies_router, prefix="/api")
