from fastapi import FastAPI

from .kafka import producer
from .routers import payments, probe

app = FastAPI()
app.include_router(payments.router)
app.include_router(probe.router)


@app.on_event("startup")
async def startup_event():
    # Get cluster layout and initial topic/partition leadership information
    await producer.start()


@app.on_event("shutdown")
async def shutdown_event():
    # Wait for all pending messages to be delivered or expire.
    await producer.stop()
