FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /app/api_valor_do_metro_quadrado

ENV MODULE_NAME=api_valor_do_metro_quadrado.main
ENV PORT=8081

COPY ./api_valor_do_metro_quadrado/ .

RUN pip install --upgrade pip && pip install -r requirements.txt
