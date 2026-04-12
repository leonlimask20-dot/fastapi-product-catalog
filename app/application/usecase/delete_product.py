from uuid import UUID
from app.domain.repository.product_repository import ProductRepository


class DeleteProductUseCase:

    def __init__(self, repository: ProductRepository) -> None:
        self._repository = repository

    def execute(self, product_id: UUID) -> bool:
        product = self._repository.find_by_id(product_id)
        if not product:
            return False
        self._repository.delete(product_id)
        return True
