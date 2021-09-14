from fastapi import FastAPI

from .http import client
from .routers import deeplinks, probe, redirect

app = FastAPI()
app.include_router(deeplinks.router)
app.include_router(probe.router)
app.include_router(redirect.router)


@app.on_event("shutdown")
async def shutdown_event():
    await client.aclose()
