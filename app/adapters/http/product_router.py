from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from app.infrastructure.database.session import get_db
from app.adapters.persistence.product_repository_impl import ProductRepositoryImpl
from app.application.usecase.create_product import CreateProductUseCase
from app.application.usecase.get_product import GetProductUseCase
from app.application.usecase.list_products import ListProductsUseCase
from app.application.usecase.update_product import UpdateProductUseCase
from app.application.usecase.delete_product import DeleteProductUseCase
from app.adapters.http.schemas import ProductRequest, ProductResponse

router = APIRouter(prefix="/api/v1/products", tags=["products"])


def _repo(db: Session = Depends(get_db)) -> ProductRepositoryImpl:
    return ProductRepositoryImpl(db)


@router.post("", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(body: ProductRequest, repo=Depends(_repo)):
    product = CreateProductUseCase(repo).execute(
        name=body.name,
        description=body.description,
        price=body.price,
        stock=body.stock,
        category=body.category,
    )
    return ProductResponse.from_domain(product)


@router.get("", response_model=list[ProductResponse])
def list_products(
    skip:     int         = Query(0, ge=0),
    limit:    int         = Query(20, ge=1, le=100),
    category: str | None  = Query(None),
    repo=Depends(_repo),
):
    products = ListProductsUseCase(repo).execute(skip=skip, limit=limit, category=category)
    return [ProductResponse.from_domain(p) for p in products]


@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: UUID, repo=Depends(_repo)):
    product = GetProductUseCase(repo).execute(product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado")
    return ProductResponse.from_domain(product)


@router.put("/{product_id}", response_model=ProductResponse)
def update_product(product_id: UUID, body: ProductRequest, repo=Depends(_repo)):
    product = UpdateProductUseCase(repo).execute(
        product_id  = product_id,
        name        = body.name,
        description = body.description,
        price       = body.price,
        stock       = body.stock,
        category    = body.category,
    )
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado")
    return ProductResponse.from_domain(product)


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: UUID, repo=Depends(_repo)):
    deleted = DeleteProductUseCase(repo).execute(product_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado")
