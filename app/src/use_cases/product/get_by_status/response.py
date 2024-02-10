from typing import List

from typing import NamedTuple

from ....core.models._product import Product


class FindProductsByStatusResponse(NamedTuple):
  products: List[Product]
