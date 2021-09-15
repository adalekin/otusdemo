from fastapi import FastAPI

from .routers import funnel, probe

app = FastAPI()
app.include_router(funnel.router)
app.include_router(probe.router)
