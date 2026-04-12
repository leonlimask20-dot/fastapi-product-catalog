from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


class ProductRequest(BaseModel):
    name:        str   = Field(..., min_length=2, max_length=200)
    description: str   = Field(..., min_length=5, max_length=1000)
    price:       float = Field(..., gt=0)
    stock:       int   = Field(..., ge=0)
    category:    str   = Field(..., min_length=2, max_length=100)


class ProductResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id:          UUID
    name:        str
    description: str
    price:       float
    stock:       int
    category:    str
    active:      bool
    in_stock:    bool
    created_at:  datetime
    updated_at:  datetime

    @classmethod
    def from_domain(cls, product) -> "ProductResponse":
        return cls(
            id          = product.id,
            name        = product.name,
            description = product.description,
            price       = product.price,
            stock       = product.stock,
            category    = product.category,
            active      = product.active,
            in_stock    = product.is_in_stock(),
            created_at  = product.created_at,
            updated_at  = product.updated_at,
        )
