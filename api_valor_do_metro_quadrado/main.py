import logging

from fastapi import FastAPI

from app.infrastructure.repository import database
from app.application.log import logger


app = FastAPI()


@app.on_event("startup")
async def startup():
    logger.info("Connecting to Database")
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    logger.info("Removing Database Connection")
    await database.disconnect()
