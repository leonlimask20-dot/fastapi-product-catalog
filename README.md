# fastapi-product-catalog

[![CI](https://github.com/leonlimask20-dot/fastapi-product-catalog/actions/workflows/ci.yml/badge.svg)](https://github.com/leonlimask20-dot/fastapi-product-catalog/actions/workflows/ci.yml)

Product catalog REST API built with **FastAPI** and **Clean Architecture**,
demonstrating Python on the backend with PostgreSQL, Alembic migrations and
cloud deployment via Render.

## Stack

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?style=flat&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?style=flat&logo=postgresql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-D71F00?style=flat)
![Alembic](https://img.shields.io/badge/Alembic-1.15-6BA81E?style=flat)
![Docker](https://img.shields.io/badge/Docker-29.x-2496ED?style=flat&logo=docker&logoColor=white)
![Render](https://img.shields.io/badge/Render-Deploy-46E3B7?style=flat&logo=render&logoColor=white)

## Architecture

```
fastapi-product-catalog/
├── app/
│   ├── domain/                 # Core — no external dependencies
│   │   ├── entity/product.py   # Rich entity with business rules
│   │   └── repository/         # Interface (port) — abstract contract
│   ├── application/
│   │   └── usecase/            # Use cases: create, get, list, update, delete
│   ├── adapters/
│   │   ├── http/               # FastAPI router + Pydantic schemas
│   │   └── persistence/        # SQLAlchemy model + repository implementation
│   └── infrastructure/
│       ├── config/settings.py  # Pydantic Settings — reads environment variables
│       └── database/session.py # Engine + SessionLocal + declarative Base
├── alembic/                    # Versioned migrations
├── main.py                     # FastAPI entry point
├── render.yaml                 # Automatic deploy on Render
└── docker-compose.yml          # Local PostgreSQL for development
```

## Endpoints

| Method | Route | Description |
|---|---|---|
| `POST` | `/api/v1/products` | Create product |
| `GET` | `/api/v1/products` | List products (pagination + category filter) |
| `GET` | `/api/v1/products/{id}` | Get product by ID |
| `PUT` | `/api/v1/products/{id}` | Update product |
| `DELETE` | `/api/v1/products/{id}` | Deactivate product (soft delete) |
| `GET` | `/health` | Health check |
| `GET` | `/docs` | Swagger UI (auto-generated) |

## Running locally

### Prerequisites
- Python 3.12+
- Docker Desktop

### 1. Clone and install dependencies

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

### 2. Configure environment variables

```bash
cp .env.example .env
```

### 3. Start PostgreSQL

```bash
docker-compose up -d postgres
```

### 4. Run the migrations

```bash
alembic upgrade head
```

### 5. Start the API

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000` and Swagger at `http://localhost:8000/docs`.

## Testing the API

```powershell
# Create product
$body = [System.Text.Encoding]::UTF8.GetBytes('{"name":"Mechanical Keyboard","description":"Mechanical keyboard with blue switches","price":299.90,"stock":15,"category":"Peripherals"}')
Invoke-RestMethod -Uri "http://localhost:8000/api/v1/products" -Method POST -ContentType "application/json; charset=utf-8" -Body $body

# List products
Invoke-RestMethod -Uri "http://localhost:8000/api/v1/products" -Method GET

# Filter by category
Invoke-RestMethod -Uri "http://localhost:8000/api/v1/products?category=Peripherals" -Method GET
```

## Concepts demonstrated

- **Clean Architecture in Python** — domain isolated from FastAPI, SQLAlchemy and HTTP
- **Rich entity** — business logic lives in the entity (`deactivate()`, `update()`, `is_in_stock()`)
- **Repository as a port** — `ProductRepository` is an ABC interface; FastAPI never touches SQLAlchemy directly
- **Pydantic v2** — request validation (`ProductRequest`) and response serialization (`ProductResponse`)
- **Pydantic Settings** — typed environment variables, read automatically from `.env`
- **Alembic** — versioned, reversible migrations (`upgrade`/`downgrade`)
- **Soft delete** — products are deactivated (`active=False`), not removed from the database
- **Deploy on Render** — `render.yaml` defines a web service + managed PostgreSQL database

## 🤖 Agent Architecture

This project was built and code-reviewed using a **multi-agent
context-optimization workflow**: specialized AI agents each audit a single
architectural layer — domain, use cases, adapters, infrastructure, tests —
within a strict context budget. The approach cuts review time and token cost
while keeping full traceability of every finding.

Methodology, agent templates and the full playbook: **[Stop Burning Context — Claude Code Playbook](https://leonlim3.gumroad.com/l/claude-code-context-playbook)**

## Related projects

- [order-processing-api](https://github.com/leonlimask20-dot/order-processing-api) — Clean Architecture + Spring Boot
- [order-notification-service](https://github.com/leonlimask20-dot/order-notification-service) — Apache Kafka + DLQ
- [k8s-microservices-demo](https://github.com/leonlimask20-dot/k8s-microservices-demo) — Kubernetes + Minikube
