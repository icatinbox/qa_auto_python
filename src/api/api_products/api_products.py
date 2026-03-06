
class ApiProducts:
    def __init__(self, client):
        self.client = client

    def get_all_products(self, params=None):
        #params: limit, skip, q, sortBy, order
        return self.client.request_json('GET', 'products', params=params)

    def get_product_by_id(self, product_id):
        return self.client.request_json('GET', f'products/{product_id}')

    def get_products_categories(self):
        return self.client.request_json('GET', 'products/categories')

    def get_products_category_list(self):
        return self.client.request_json('GET', 'products/category-list')

    def get_products_by_category(self, category):
        return self.client.request_json('GET', f'products/category/{category}')

    def add_new_product(self, payload=None):
        return self.client.request_json('POST', f'products/add', json=payload)

    def delete_product(self, product_id):
        return self.client.request_json('DELETE', f'products/{product_id}')

    def update_patch_product(self, product_id, payload=None):
        return self.client.request_json('PATCH', f'products/{product_id}', json=payload)

    def update_put_product(self, product_id, payload=None):
        return self.client.request_json('PUT', f'products/{product_id}', json=payload)