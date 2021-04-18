import logging

from fastapi import FastAPI

from app.infrastructure.repository import database


app = FastAPI()


@app.on_event("startup")
async def startup():
    logging.info("Connecting to Database")
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()
