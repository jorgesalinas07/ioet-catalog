from http import HTTPStatus

from fastapi.testclient import TestClient


def test__should_return_a_list_of_products(api_client: TestClient):
    expected_products = 3

    response = api_client.get("/products/")
    products = response.json().get("products")

    assert response.status_code == HTTPStatus.OK
    assert len(products) == expected_products
