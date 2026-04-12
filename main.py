from fastapi import FastAPI
from app.adapters.http.product_router import router
from app.infrastructure.config.settings import settings

app = FastAPI(
    title=settings.app_name,
    description="API REST de catálogo de produtos — Clean Architecture com FastAPI e PostgreSQL",
    version="1.0.0",
)

app.include_router(router)


@app.get("/health")
def health():
    return {"status": "ok"}
