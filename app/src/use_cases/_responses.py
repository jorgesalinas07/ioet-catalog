from decimal import Decimal

from pydantic import BaseModel

from ..core.enums import ProductStatuses


class GetProductResponse(BaseModel):
    id: str
    name: str
    price: Decimal
    status: ProductStatuses
    is_available: bool


class GetProductsResponse(BaseModel):
    products: list[GetProductResponse]
