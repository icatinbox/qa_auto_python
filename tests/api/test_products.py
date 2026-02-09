import pytest

def test_get_products(api_auth_products):
    data = api_auth_products.get_all_products()
    assert isinstance(data['products'], list)
    assert len(data['products']) == 30
    assert 'id' in data['products'][0]

@pytest.mark.parametrize('limit', [10, 20, 50, 100])
def test_count_limit_products(api_auth_products, limit):
    params = {'limit': limit}
    data = api_auth_products.get_all_products(params=params)
    assert len(data['products']) == limit
    assert data['limit'] == limit

def test_skip_products(api_auth_products):
    params = {'skip': 30}
    data = api_auth_products.get_all_products(params=params)
    assert len(data['products']) == 30
    assert data['products'][0]['id'] == 31
    assert data['skip'] == 30

def test_search_product(api_auth_products):
    params = {'q': 'phone'}
    data = api_auth_products.get_all_products(params=params)
    assert len(data['products']) > 0

def test_get_product_by_id(api_auth_products, id_product):
    data = api_auth_products.get_product_by_id(id_product)
    assert data['id'] == id_product
    assert isinstance(data, dict)
