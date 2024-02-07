from adapters.src.repositories import MemoryProductRepository, SQLProductRepository, SessionManager
from app.src.repositories import ProductRepository

def memory_product_repository() -> ProductRepository:
  return MemoryProductRepository

def sql_product_repository() -> ProductRepository:
  return SQLProductRepository(SessionManager.get_session())
