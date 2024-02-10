import pytest
from app.src.exceptions.repository.product import ProductRepositoryException
from app.src.use_cases.product.get_by_status.request import FindProductsByStatusRequest
from app.src.use_cases.product.get_by_status.response import FindProductsByStatusResponse
from app.src.use_cases.product.get_by_status.use_case import FindProductsByStatus
from app.src.core.models._product import Product

products = [
    Product(
        product_id = '1',
        user_id = '1',
        name = 'fake_name_1',
        description = 'fake_description_1',
        price = 10.5,
        location = 'fake_location_1',
        status = 'New',
        is_available = True,
    ),
    Product(
        product_id = '2',
        user_id = '2',
        name = 'fake_name_2',
        description = 'fake_description_2',
        price = 10.5,
        location = 'fake_location_2',
        status = 'New',
        is_available = True,
    )
]


def test_find_product_by_status_return_products_successfully(mocker):
    product_repository = mocker.Mock()
    product_repository.get_by_status = mocker.Mock(return_value=products)
    use_case = FindProductsByStatus(product_repository)
    request = FindProductsByStatusRequest(status='New')

    response = use_case(request=request)

    assert isinstance(response, FindProductsByStatusResponse)
    assert len(response.products) == 2

def test_find_product_by_status_raise_product_repository_exception_when_database_error(
    mocker
):
    product_repository = mocker.Mock()
    product_repository.get_by_status = mocker.Mock(side_effect=ProductRepositoryException(method="find"))
    use_case = FindProductsByStatus(product_repository)
    request = FindProductsByStatusRequest(status='New')

    with pytest.raises(ProductRepositoryException) as exc_info:
        use_case(request=request)

    assert str(exc_info.value) == "Exception while executing find in Product"
