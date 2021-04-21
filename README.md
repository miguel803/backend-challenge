# inGaia - Back-end Developer  ![Build Status](https://travis-ci.org/miguel803/backend-challenge.svg?branch=main)

## Instruções para Execução dos Microsserviços

### Para executar o projeto na máquina local será necessário ter configurado Docker e Docker-Compose

- git clone https://github.com/migueleichler/backend-challenge.git

- docker-compose up --build

- para testar o fluxo principal basta realizar uma consulta na API 2. Exemplo: http://localhost:8082/imovel/?metragem=100

## Documentação das API's:

- Api 1: localhost:8081/docs

- Api 2: localhost:8082/docs

## Padrão de Arquitetura

- O projeto foi estruturado com base no padrão de arquitetura Domain Driven Design, criado por Eric Evans.

- O projeto está dividido em três camadas principais: Aplicação, Domínio e Infraestrutura

![Imagem Ilustrativa](https://github.com/miguel803/backend-challenge/blob/main/docs/arquitetura/ddd-layers.png)
