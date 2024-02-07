from pydantic import BaseModel

from ..core.enums import ProductStatuses


class GetProductsRequest(BaseModel):
    status: ProductStatuses | None
