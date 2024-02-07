from .base import RepositoryConfig
from factories.repositories import memory_product_repository, sql_product_repository

class CatalogRepositoryConfig(RepositoryConfig):
  _AVAILABLE_REPOSITORIES: list[str] = ["MEMORY", "SQL"]

  @classmethod
  def _get_repository_instances(cls) -> dict:
    return {
      "MEMORY": memory_product_repository(),
      "SQL": sql_product_repository()
    }
