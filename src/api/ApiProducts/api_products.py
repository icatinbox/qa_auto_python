
class ApiProducts:
    def __init__(self, client):
        self.client = client

    def get_all_products(self, params=None):
        #params: limit, skip, q, sortBy, order
        return self.client.request_json('GET', '/products', params=params)

    def get_product_by_id(self, product_id):
        return self.client.request_json('GET', f'/products/{product_id}')

    def get_all_products_categories(self, params):
        return self.client.request_json('GET', '/products/categories', params=params)