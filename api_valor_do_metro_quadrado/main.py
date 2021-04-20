import logging

from fastapi import FastAPI

from api_valor_do_metro_quadrado.infrastructure.repositories import database
from api_valor_do_metro_quadrado.application.log import logger
from api_valor_do_metro_quadrado.application.routes import metro_quadrado


app = FastAPI()


@app.on_event("startup")
async def startup():
    logger.info("Connecting to Database")
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    logger.info("Removing Database Connection")
    await database.disconnect()


app.include_router(metro_quadrado.router)
