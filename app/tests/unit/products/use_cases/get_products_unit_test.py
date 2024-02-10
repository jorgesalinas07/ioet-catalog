import pytest
from app.src.exceptions.business.product import ProductBusinessException, ProductNotFoundException
from app.src.exceptions.repository.product import ProductRepositoryException
from app.src.use_cases.product.edit.request import EditProductRequest
from app.src.use_cases.product.edit.response import EditProductResponse
from app.src.use_cases.product.edit.use_case import EditProduct
from app.src.use_cases.product.get_by_status.request import FindProductsByStatusRequest
from app.src.use_cases.product.get_by_status.response import FindProductsByStatusResponse
from app.src.use_cases.product.get_by_status.use_case import FindProductsByStatus
from app.src.core.models._product import Product

# Implement fixtures and faker in future tickets
product = Product(
        product_id = '1',
        user_id = '1',
        name = 'fake_name_1',
        description = 'fake_description_1',
        price = 10.5,
        location = 'fake_location_1',
        status = 'New',
        is_available = True,
    )

edited_product = Product(
    product_id = '1',
    user_id = '1',
    name = 'fake_name_edited',
    description = 'fake_description_edited',
    price = 10.5,
    location = 'fake_location_edited',
    status = 'Used',
    is_available = True,
)

products = [
    product,
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

def test_edit_product_edits_successfully(mocker):
    product_repository = mocker.Mock()
    product_repository.get_by_id = mocker.Mock(return_value=product)
    product_repository.edit = mocker.Mock(return_value=edited_product)

    use_case = EditProduct(product_repository)
    request = EditProductRequest(
        product_id='fake_product_id',
        user_id='fake_user_id',
        name='fake_name',
        description='fake_description',
        price='fake_price',
        location='fake_location',
        status='fake_status',
        is_available=True,
    )

    response = use_case(request=request)

    assert isinstance(response, EditProductResponse)
    assert response.description == 'fake_description_edited'
    assert response.name == 'fake_name_edited'
    assert response.location == 'fake_location_edited'
    assert response.status == 'Used'

def test_edit_product_raise_product_repository_exception_when_database_error(
    mocker
):
    product_repository = mocker.Mock()
    product_repository.get_by_id = mocker.Mock(return_value=product)
    product_repository.edit = mocker.Mock(side_effect=ProductRepositoryException(method="edit"))
    use_case = EditProduct(product_repository)
    request = EditProductRequest(
        product_id='fake_product_id',
        user_id='fake_user_id',
        name='fake_name',
        description='fake_description',
        price='fake_price',
        location='fake_location',
        status='fake_status',
        is_available=True,
    )

    with pytest.raises(ProductBusinessException) as exc_info:
        use_case(request=request)

    assert str(exc_info.value) == "Exception while executing edit in Product"

def test_edit_product_raise_product_not_found_exception_when_no_product_in_database(
    mocker
):
    product_repository = mocker.Mock()
    product_repository.get_by_id = mocker.Mock(return_value=None)
    use_case = EditProduct(product_repository)
    request = EditProductRequest(
        product_id='fake_product_id',
        user_id='fake_user_id',
        name='fake_name',
        description='fake_description',
        price='fake_price',
        location='fake_location',
        status='fake_status',
        is_available=True,
    )

    with pytest.raises(ProductNotFoundException):
        use_case(request=request)
