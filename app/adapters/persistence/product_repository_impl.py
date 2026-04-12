from uuid import UUID
from typing import Optional
from sqlalchemy.orm import Session
from app.domain.entity.product import Product
from app.domain.repository.product_repository import ProductRepository
from app.adapters.persistence.product_model import ProductModel


class ProductRepositoryImpl(ProductRepository):

    def __init__(self, db: Session) -> None:
        self._db = db

    def save(self, product: Product) -> Product:
        existing = self._db.get(ProductModel, product.id)
        if existing:
            existing.name        = product.name
            existing.description = product.description
            existing.price       = product.price
            existing.stock       = product.stock
            existing.category    = product.category
            existing.active      = product.active
            existing.updated_at  = product.updated_at
            self._db.commit()
            self._db.refresh(existing)
            return existing.to_domain()
        model = ProductModel.from_domain(product)
        self._db.add(model)
        self._db.commit()
        self._db.refresh(model)
        return model.to_domain()

    def find_by_id(self, product_id: UUID) -> Optional[Product]:
        model = self._db.get(ProductModel, product_id)
        return model.to_domain() if model else None

    def find_all(self, skip: int = 0, limit: int = 20) -> list[Product]:
        models = self._db.query(ProductModel).filter(ProductModel.active == True).offset(skip).limit(limit).all()
        return [m.to_domain() for m in models]

    def find_by_category(self, category: str) -> list[Product]:
        models = self._db.query(ProductModel).filter(
            ProductModel.category == category,
            ProductModel.active == True
        ).all()
        return [m.to_domain() for m in models]

    def delete(self, product_id: UUID) -> None:
        model = self._db.get(ProductModel, product_id)
        if model:
            model.active = False
            self._db.commit()
