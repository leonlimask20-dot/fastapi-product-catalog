from abc import ABC, abstractmethod
from uuid import UUID
from typing import Optional
from app.domain.entity.product import Product


class ProductRepository(ABC):

    @abstractmethod
    def save(self, product: Product) -> Product:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, product_id: UUID) -> Optional[Product]:
        raise NotImplementedError

    @abstractmethod
    def find_all(self, skip: int = 0, limit: int = 20) -> list[Product]:
        raise NotImplementedError

    @abstractmethod
    def find_by_category(self, category: str) -> list[Product]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, product_id: UUID) -> None:
        raise NotImplementedError
