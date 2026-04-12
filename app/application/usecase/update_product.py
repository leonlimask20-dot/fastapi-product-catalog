from uuid import UUID
from typing import Optional
from app.domain.entity.product import Product
from app.domain.repository.product_repository import ProductRepository


class UpdateProductUseCase:

    def __init__(self, repository: ProductRepository) -> None:
        self._repository = repository

    def execute(self, product_id: UUID, name: str, description: str, price: float, stock: int, category: str) -> Optional[Product]:
        product = self._repository.find_by_id(product_id)
        if not product:
            return None
        product.update(name=name, description=description, price=price, stock=stock, category=category)
        return self._repository.save(product)
