from app.domain.entity.product import Product
from app.domain.repository.product_repository import ProductRepository


class CreateProductUseCase:

    def __init__(self, repository: ProductRepository) -> None:
        self._repository = repository

    def execute(self, name: str, description: str, price: float, stock: int, category: str) -> Product:
        product = Product(
            name=name,
            description=description,
            price=price,
            stock=stock,
            category=category,
        )
        return self._repository.save(product)
