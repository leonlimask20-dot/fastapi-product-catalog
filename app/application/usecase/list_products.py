from app.domain.entity.product import Product
from app.domain.repository.product_repository import ProductRepository


class ListProductsUseCase:

    def __init__(self, repository: ProductRepository) -> None:
        self._repository = repository

    def execute(self, skip: int = 0, limit: int = 20, category: str | None = None) -> list[Product]:
        if category:
            return self._repository.find_by_category(category)
        return self._repository.find_all(skip=skip, limit=limit)
