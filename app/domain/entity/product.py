from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4


@dataclass
class Product:
    name: str
    description: str
    price: float
    stock: int
    category: str
    id: UUID = field(default_factory=uuid4)
    active: bool = True
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)

    def deactivate(self) -> None:
        self.active = False
        self.updated_at = datetime.utcnow()

    def update(self, name: str, description: str, price: float, stock: int, category: str) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        self.category = category
        self.updated_at = datetime.utcnow()

    def is_in_stock(self) -> bool:
        return self.stock > 0
