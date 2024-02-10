from typing import Optional

from app.src.core import Product
from app.src.exceptions.business.product import ProductNotFoundException
from app.src.repositories import ProductRepository
from app.src.exceptions import ProductRepositoryException, ProductBusinessException

from .response import EditProductResponse
from .request import EditProductRequest


class EditProduct:
  def __init__(self, product_repository: ProductRepository) -> None:
    self.product_repository = product_repository

  def __call__(self, request: EditProductRequest) -> Optional[EditProductResponse]:
    product = Product(**request._asdict())
    try:
      self._verify_product_existence(product_id=request.product_id)
      response: Optional[Product] = self.product_repository.edit(product)

      return EditProductResponse(**response._asdict())
    except ProductRepositoryException as e:
      raise ProductBusinessException(str(e))

  def _verify_product_existence(self, product_id):
    product_existing = self.product_repository.get_by_id(product_id)
    if not product_existing:
      raise ProductNotFoundException(product_id=product_id)
