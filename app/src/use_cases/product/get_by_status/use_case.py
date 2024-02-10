from app.src.exceptions import (
  ProductRepositoryException,
)

from app.src.repositories import ProductRepository

from .request import FindProductsByStatusRequest
from .response import FindProductsByStatusResponse


class FindProductsByStatus:
  def __init__(self, product_repository: ProductRepository) -> None:
    self.product_repository = product_repository

  def __call__(self, request: FindProductsByStatusRequest) -> FindProductsByStatusResponse:
    try:
      products = self.product_repository.get_by_status(request.status)
      return FindProductsByStatusResponse(products=products)
    except ProductRepositoryException as e:
      raise e
