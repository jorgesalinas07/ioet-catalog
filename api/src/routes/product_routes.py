from fastapi import APIRouter, Depends, Query

from app.src.use_cases import (
    ListProducts, 
    ListProductResponse, 
    FindProductById, 
    FindProductByIdResponse, 
    FindProductByIdRequest, 
    CreateProduct, 
    CreateProductResponse, 
    CreateProductRequest,
    FindProductsByStatus,
    FindProductsByStatusResponse,
    FindProductsByStatusRequest,
    EditProduct,
    EditProductRequest,
    EditProductResponse,
)
from ..dtos import (
    ProductBase,
    ListProductResponseDto, 
    CreateProductRequestDto,
    CreateProductResponseDto,
    FindProductByIdResponseDto,
    FindProductsByStatusResponseDto,
    EditProductResponseDto,
    EditProductRequestDto,
)
from factories.use_cases import (
    list_product_use_case, 
    find_product_by_id_use_case,
    create_product_use_case,
    find_product_by_status_use_case,
    edit_product_use_case,
)

product_router = APIRouter(prefix="/products")

@product_router.get("/", response_model=ListProductResponseDto)
async def get_products(
    use_case: ListProducts = Depends(list_product_use_case)
) -> ListProductResponse:
    response = use_case()
    response_dto: ListProductResponseDto = ListProductResponseDto(
        products= [ProductBase(**product._asdict()) for product in response.products]
    )
    return response_dto

@product_router.get("/{product_id}", response_model=FindProductByIdResponseDto)
async def get_product_by_id(
    product_id: str,
    use_case: FindProductById = Depends(find_product_by_id_use_case)
) -> FindProductByIdResponse:
    response = use_case(FindProductByIdRequest(product_id=product_id))
    response_dto: FindProductByIdResponseDto = FindProductByIdResponseDto(**response._asdict())
    return response_dto

@product_router.post("/", response_model=CreateProductResponseDto)
async def create_product(
    request: CreateProductRequestDto,
    use_case: CreateProduct = Depends(create_product_use_case)
) -> CreateProductResponse:
    response = use_case(CreateProductRequest(
        product_id=request.product_id, 
        user_id=request.user_id, 
        name=request.name, 
        description=request.description, 
        price=request.price, 
        location=request.location, 
        status=request.status, 
        is_available=request.is_available
    ))
    response_dto: CreateProductResponseDto = CreateProductResponseDto(**response._asdict())
    return response_dto

@product_router.get("", response_model=FindProductsByStatusResponseDto)
async def get_products_by_status(
    status: str = Query(None, description="Filter products by status (e.g., 'New', 'Used', 'For parts')"),
    use_case: FindProductsByStatus = Depends(find_product_by_status_use_case),
) -> FindProductsByStatusResponse:
    # Implement status code error handling in future tickets
    response = use_case(FindProductsByStatusRequest(status=status))
    response_dto: FindProductsByStatusResponseDto = FindProductsByStatusResponseDto(
        products= [ProductBase(**product._asdict()) for product in response.products]
    )
    return response_dto

@product_router.put("/{product_id}", response_model=EditProductResponseDto)
async def edit_product(
    product_id: str,
    request: EditProductRequestDto,
    use_case: EditProduct = Depends(edit_product_use_case),
) -> EditProductResponse:
    # Implement status code error handling in future tickets
    response = use_case(EditProductRequest(
        product_id=product_id,
        user_id=request.user_id,
        name=request.name,
        description=request.description,
        price=request.price,
        location=request.location,
        status=request.status,
        is_available=request.is_available
    ))

    response_dto: FindProductByIdResponseDto = FindProductByIdResponseDto(**response._asdict())
    return response_dto
