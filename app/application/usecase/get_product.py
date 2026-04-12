from uuid import UUID
from typing import Optional
from app.domain.entity.product import Product
from app.domain.repository.product_repository import ProductRepository


class GetProductUseCase:

    def __init__(self, repository: ProductRepository) -> None:
        self._repository = repository

    def execute(self, product_id: UUID) -> Optional[Product]:
        return self._repository.find_by_id(product_id)
