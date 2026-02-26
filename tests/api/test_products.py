import random
import pytest
from tests.schemas.all_products_schema import AllProductsResponse, Product


def test_get_all_products(api_auth_products):
    response, data = api_auth_products.get_all_products(params={'limit': 0})
    result = AllProductsResponse.model_validate(data)
    ids = [p.id for p in result.products]
    assert len(ids) == len(set(ids))

@pytest.mark.parametrize('limit', [30, 50, 100])
def test_count_limit_products(api_auth_products, limit):
    params = {'limit': limit}
    response, data = api_auth_products.get_all_products(params=params)
    assert len(data['products']) <= limit
    assert data['total'] >= len(data['products'])
    assert data['limit'] == limit
    assert response.elapsed.total_seconds() < 2.0

@pytest.mark.parametrize('skip', [30, 50, 100])
def test_skip_products(api_auth_products, skip):
    params = {'skip': skip}
    _, data = api_auth_products.get_all_products(params=params)
    result = AllProductsResponse.model_validate(data)
    assert len(result.products) <= result.limit
    assert result.skip == skip

def test_pagination(api_auth_products):
    params1 = {'limit': 30, 'skip': 0}
    params2 = {'limit': 30, 'skip': 30}
    _1, data1 = api_auth_products.get_all_products(params=params1)
    _2, data2 = api_auth_products.get_all_products(params=params2)
    ids1 = {data.id for data in data1['products']}
    ids2 = {data.id for data in data2['products']}
    assert data1['limit'] == 30
    assert data1['skip'] == 0
    assert data2['limit'] == 30
    assert data2['skip'] == 30
    # Добавить стабильности, если элементов мало
    # if data1['total'] > data1['limit']:
    assert ids1.isdisjoint(ids2)

@pytest.mark.parametrize('q', ['phone', '123'])
def test_search_product(api_auth_products, q):
    params = {'q': q}
    _, data = api_auth_products.get_all_products(params=params)
    result = AllProductsResponse.model_validate(data)
    assert len(result.products) > 0

# Фикстура делает каждый раз новый запрос, а нам достаточно одного и из него уже выбирать значения
@pytest.mark.parametrize('i', range(5))
def test_get_product_by_id(api_auth_products, total_product, i):
    id_product = random.randint(1, total_product)
    _, data = api_auth_products.get_product_by_id(id_product)
    result = Product.model_validate(data)
    assert result.id == id_product
