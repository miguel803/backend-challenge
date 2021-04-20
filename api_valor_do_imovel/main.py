from fastapi import FastAPI

from api_valor_do_imovel.application.routes import imovel


app = FastAPI()

app.include_router(imovel.router)
