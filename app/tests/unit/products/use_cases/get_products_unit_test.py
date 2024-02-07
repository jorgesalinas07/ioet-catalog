from app.products.use_cases import (GetProductsCase, GetProductsReponse,
                                    GetProductsRequest)


class TestGetProductsCase:
    def test__returns_a_list_of_products(self):
        expected_products = 3
        request = GetProductsRequest(status=None)
        use_case = GetProductsCase()

        response = use_case(request=request)

        assert isinstance(response, GetProductsReponse)
        assert len(response.products) == expected_products
