from decimal import Decimal

from ..core.enums import ProductStatuses
from ..core.models import Product
from ._requests import GetProductsRequest
from ._responses import GetProductResponse, GetProductsResponse


class GetProductsCase:
    def __call__(self, request: GetProductsRequest) -> GetProductResponse:
        all_products = [
            Product(
                id="1",
                user_id="1",
                name="Headphones",
                description="Noise cancellation",
                price=Decimal(10.5),
                location="Quito",
                status=ProductStatuses.USED,
                is_available=True,
            ),
            Product(
                id="2",
                user_id="2",
                name="Jacket",
                description="Official ioet jacket",
                price=Decimal(20),
                location="Loja",
                status=ProductStatuses.USED,
                is_available=True,
            ),
            Product(
                id="3",
                user_id="3",
                name="Mac mini",
                description="With the M1 chip",
                price=Decimal(20),
                location="Guayaquil",
                status=ProductStatuses.NEW,
                is_available=False,
            ),
        ]
        if request.status:
            filter_products = filter(
                lambda product: product.status == request.status, all_products
            )
            return GetProductsResponse(
                products=[
                    GetProductResponse(**product.dict())
                    for product in list(filter_products)
                ]
            )
        return GetProductsResponse(
            products=[GetProductResponse(**product.dict()) for product in all_products]
        )
