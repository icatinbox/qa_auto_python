import random

import pytest
from tests.schemas.all_products_schema import AllProductsResponse, Product


def test_get_products(api_auth_products):
    data = api_auth_products.get_all_products()
    result = AllProductsResponse.model_validate(data)
    assert result.limit == 30
    assert all(p.id > 0 for p in result.products)

@pytest.mark.parametrize('limit', [10, 20, 50, 100])
def test_count_limit_products(api_auth_products, limit):
    params = {'limit': limit}
    data = api_auth_products.get_all_products(params=params)
    result = AllProductsResponse.model_validate(data)
    assert len(result.products) == limit
    assert result.limit == limit

@pytest.mark.parametrize('skip', [10, 20, 50, 100])
def test_skip_products(api_auth_products, skip):
    params = {'skip': skip}
    data = api_auth_products.get_all_products(params=params)
    result = AllProductsResponse.model_validate(data)
    assert len(result.products) == 30
    assert result.skip == skip

@pytest.mark.parametrize('q', ['phone', '123'])
def test_search_product(api_auth_products, q):
    params = {'q': q}
    data = api_auth_products.get_all_products(params=params)
    result = AllProductsResponse.model_validate(data)
    assert len(result.products) > 0

@pytest.mark.parametrize('i', range(5))
def test_get_product_by_id(api_auth_products, total_product, i):
    id_product = random.randint(1, total_product)
    data = api_auth_products.get_product_by_id(id_product)
    result = Product.model_validate(data)
    print(result.id)
    assert result.id == id_product
