from sqlalchemy import Column, String, Float, Integer, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID as PgUUID
from datetime import datetime
import uuid
from app.infrastructure.database.session import Base
from app.domain.entity.product import Product


class ProductModel(Base):
    __tablename__ = "products"

    id          = Column(PgUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name        = Column(String(200), nullable=False)
    description = Column(String(1000), nullable=False)
    price       = Column(Float, nullable=False)
    stock       = Column(Integer, nullable=False, default=0)
    category    = Column(String(100), nullable=False)
    active      = Column(Boolean, nullable=False, default=True)
    created_at  = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at  = Column(DateTime, nullable=False, default=datetime.utcnow)

    def to_domain(self) -> Product:
        p = Product.__new__(Product)
        p.id          = self.id
        p.name        = self.name
        p.description = self.description
        p.price       = self.price
        p.stock       = self.stock
        p.category    = self.category
        p.active      = self.active
        p.created_at  = self.created_at
        p.updated_at  = self.updated_at
        return p

    @staticmethod
    def from_domain(product: Product) -> "ProductModel":
        return ProductModel(
            id          = product.id,
            name        = product.name,
            description = product.description,
            price       = product.price,
            stock       = product.stock,
            category    = product.category,
            active      = product.active,
            created_at  = product.created_at,
            updated_at  = product.updated_at,
        )
