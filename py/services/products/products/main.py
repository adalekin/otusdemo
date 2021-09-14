from fastapi import FastAPI
from sqlalchemy import engine

from .database import Base, engine
from .routers import probe, products, reservations

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(products.router)
app.include_router(reservations.router)
app.include_router(probe.router)
