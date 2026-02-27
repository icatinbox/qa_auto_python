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
    result = AllProductsResponse.model_validate(data)
    assert len(result.products) <= limit
    assert result.total >= len(result.products)
    assert result.limit == limit
    assert response.elapsed.total_seconds() < 1.0

@pytest.mark.parametrize('skip', [30, 50, 100])
def test_skip_products(api_auth_products, skip):
    params = {'skip': skip}
    response, data = api_auth_products.get_all_products(params=params)
    result = AllProductsResponse.model_validate(data)
    assert len(result.products) <= result.limit
    assert result.skip == skip
    assert response.elapsed.total_seconds() < 1.0

def test_pagination_products(api_auth_products):
    params1 = {'limit': 30, 'skip': 0}
    params2 = {'limit': 30, 'skip': 30}
    _1, data1 = api_auth_products.get_all_products(params=params1)
    _2, data2 = api_auth_products.get_all_products(params=params2)
    result1 = AllProductsResponse.model_validate(data1)
    result2 = AllProductsResponse.model_validate(data2)
    ids1 = {data.id for data in result1.products}
    ids2 = {data.id for data in result2.products}
    assert result1.limit == 30
    assert result1.skip == 0
    assert result2.limit == 30
    assert result2.skip == 30
    assert ids1.isdisjoint(ids2)

#Добавить создание обьекта с нужным именем перед поиском
@pytest.mark.parametrize('q', ['phone', '123'])
def test_search_product(api_auth_products, q):
    params = {'q': q}
    response, data = api_auth_products.get_all_products(params=params)
    result = AllProductsResponse.model_validate(data)
    assert len(result.products) > 0
    assert response.elapsed.total_seconds() < 1.0

# Фикстура делает каждый раз новый запрос, а нам достаточно одного и из него уже выбирать значения
# подумать как оптимизировать
@pytest.mark.parametrize('i', range(5))
def test_get_product_by_id(api_auth_products, total_product, i):
    id_product = random.randint(1, total_product)
    response, data = api_auth_products.get_product_by_id(id_product)
    result = Product.model_validate(data)
    assert result.id == id_product
    assert response.elapsed.total_seconds() < 1.0

@pytest.mark.parametrize('sort, order', (
    ('title', 'desc'),
    ('title', 'asc'),
    ('price', 'desc'),
    ('price', 'asc'),
    ('rating', 'desc'),
    ('rating', 'asc'),
))
def test_sort_and_order_products(api_auth_products, sort, order):
    params = {'sortBy': sort,'order': order}
    response, data = api_auth_products.get_all_products(params=params)
    result = AllProductsResponse.model_validate(data)
    values = [getattr(p, sort) for p in result.products]
    assert response.elapsed.total_seconds() < 1.0
    if order == 'asc':
        assert all(values[i] <= values[i + 1] for i in range(len(values) - 1)), values
    elif order == 'desc':
        assert all(values[i] >= values[i + 1] for i in range(len(values) - 1)), values
    else:
        raise ValueError('Invalid order')

@pytest.mark.parametrize('sort', ['title', 'price', 'rating'])
def test_asc_vs_desc_products(api_auth_products, sort):
    params_asc = {'limit': 0, 'sortBy': sort,'order': 'asc'}
    params_desc = {'limit': 0, 'sortBy': sort,'order': 'desc'}
    response_asc, data_acs = api_auth_products.get_all_products(params=params_asc)
    response_desc, data_desc = api_auth_products.get_all_products(params=params_desc)
    result_asc = AllProductsResponse.model_validate(data_acs)
    result_desc = AllProductsResponse.model_validate(data_desc)

    asc_field = [getattr(p, sort) for p in result_asc.products]
    desc_field = [getattr(p, sort) for p in result_desc.products]

    assert min(asc_field) == desc_field[-1]
    assert max(asc_field) == desc_field[0]
