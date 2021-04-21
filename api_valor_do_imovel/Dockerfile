FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /app/api_valor_do_imovel

ENV MODULE_NAME=api_valor_do_imovel.main
ENV PORT=8082

COPY ./api_valor_do_imovel/ .

RUN pip install --upgrade pip && pip install -r requirements.txt