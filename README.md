# fastapi-product-catalog

[![CI](https://github.com/leonlimask20-dot/fastapi-product-catalog/actions/workflows/ci.yml/badge.svg)](https://github.com/leonlimask20-dot/fastapi-product-catalog/actions/workflows/ci.yml)

API REST de catálogo de produtos construída com **FastAPI** e **Clean Architecture**, demonstrando o uso de Python no backend com PostgreSQL, Alembic migrations e deploy na nuvem via Render.

## Stack

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?style=flat&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?style=flat&logo=postgresql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-D71F00?style=flat)
![Alembic](https://img.shields.io/badge/Alembic-1.15-6BA81E?style=flat)
![Docker](https://img.shields.io/badge/Docker-29.x-2496ED?style=flat&logo=docker&logoColor=white)
![Render](https://img.shields.io/badge/Render-Deploy-46E3B7?style=flat&logo=render&logoColor=white)

## Arquitetura

```
fastapi-product-catalog/
├── app/
│   ├── domain/                 # Núcleo — sem dependências externas
│   │   ├── entity/product.py   # Entidade rica com regras de negócio
│   │   └── repository/         # Interface (porta) — contrato abstrato
│   ├── application/
│   │   └── usecase/            # Casos de uso: create, get, list, update, delete
│   ├── adapters/
│   │   ├── http/               # Router FastAPI + Schemas Pydantic
│   │   └── persistence/        # SQLAlchemy model + implementação do repositório
│   └── infrastructure/
│       ├── config/settings.py  # Pydantic Settings — lê variáveis de ambiente
│       └── database/session.py # Engine + SessionLocal + Base declarativa
├── alembic/                    # Migrations versionadas
├── main.py                     # Ponto de entrada FastAPI
├── render.yaml                 # Deploy automático no Render
└── docker-compose.yml          # PostgreSQL local para desenvolvimento
```

## Endpoints

| Método | Rota | Descrição |
|---|---|---|
| `POST` | `/api/v1/products` | Criar produto |
| `GET` | `/api/v1/products` | Listar produtos (paginação + filtro por categoria) |
| `GET` | `/api/v1/products/{id}` | Buscar produto por ID |
| `PUT` | `/api/v1/products/{id}` | Atualizar produto |
| `DELETE` | `/api/v1/products/{id}` | Desativar produto (soft delete) |
| `GET` | `/health` | Health check |
| `GET` | `/docs` | Swagger UI (gerado automaticamente) |

## Como executar localmente

### Pré-requisitos
- Python 3.12+
- Docker Desktop

### 1. Clonar e instalar dependências

```bash
git clone https://github.com/leonlimask20-dot/fastapi-product-catalog.git
cd fastapi-product-catalog

python -m venv .venv
# Windows:
.venv\Scripts\Activate.ps1
# Linux/Mac:
source .venv/bin/activate

pip install -r requirements.txt
```

### 2. Configurar variáveis de ambiente

```bash
cp .env.example .env
```

### 3. Subir o PostgreSQL

```bash
docker-compose up -d postgres
```

### 4. Rodar as migrations

```bash
alembic upgrade head
```

### 5. Iniciar a API

```bash
uvicorn main:app --reload
```

A API estará disponível em `http://localhost:8000` e o Swagger em `http://localhost:8000/docs`.

## Testando a API

```powershell
# Criar produto
$body = [System.Text.Encoding]::UTF8.GetBytes('{"name":"Teclado Mecanico","description":"Teclado mecanico switch blue ABNT2","price":299.90,"stock":15,"category":"Perifericos"}')
Invoke-RestMethod -Uri "http://localhost:8000/api/v1/products" -Method POST -ContentType "application/json; charset=utf-8" -Body $body

# Listar produtos
Invoke-RestMethod -Uri "http://localhost:8000/api/v1/products" -Method GET

# Filtrar por categoria
Invoke-RestMethod -Uri "http://localhost:8000/api/v1/products?category=Perifericos" -Method GET
```

## Conceitos demonstrados

- **Clean Architecture em Python** — domínio isolado de FastAPI, SQLAlchemy e HTTP
- **Entidade rica** — lógica de negócio na entidade (`deactivate()`, `update()`, `is_in_stock()`)
- **Repositório como porta** — `ProductRepository` é uma interface ABC; o FastAPI nunca toca o SQLAlchemy diretamente
- **Pydantic v2** — validação de request (`ProductRequest`) e serialização de response (`ProductResponse`)
- **Pydantic Settings** — variáveis de ambiente tipadas, lidas automaticamente do `.env`
- **Alembic** — migrations versionadas e reversíveis (`upgrade`/`downgrade`)
- **Soft delete** — produtos são desativados (`active=False`), não removidos do banco
- **Deploy no Render** — `render.yaml` define serviço web + banco PostgreSQL gerenciado

## Projetos relacionados

- [order-processing-api](https://github.com/leonlimask20-dot/order-processing-api) — Clean Architecture + Spring Boot
- [order-notification-service](https://github.com/leonlimask20-dot/order-notification-service) — Apache Kafka + DLQ
- [k8s-microservices-demo](https://github.com/leonlimask20-dot/k8s-microservices-demo) — Kubernetes + Minikube
