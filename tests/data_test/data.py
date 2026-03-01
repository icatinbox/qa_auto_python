import copy
import string
import random
from datetime import datetime

def random_sku(length:int = 12):
    alphabet = string.ascii_uppercase + string.digits
    return ''.join(random.choice(alphabet) for _ in range(length))

def random_email(length:int = 12):
    alphabet = string.ascii_lowercase + string.digits
    start_part = ''.join(random.choice(alphabet) for _ in range(length))
    return f'{start_part}@test.com'

def random_string(length=10, word_count=1):
    space_count = word_count - 1
    letter_total  = length - space_count
    word_lengths = [1] * word_count
    remaining_letters = letter_total - word_count

    for _ in range(remaining_letters):
        word_lengths[random.randint(0, word_count - 1)] += 1

    word = [
        ''.join(random.choice(string.ascii_lowercase) for _ in range(word_length))
        for word_length in word_lengths
    ]

    return ' '.join(word)

BASE_PRODUCT_PAYLOAD = {"title": random_string(15, 2), "description": random_string(50, 7), "category": "test",
                           "price": round(random.uniform(0.1, 999.99), 2), "discountPercentage": random.randint(0, 99),
                           "rating": round(random.uniform(0.00, 5.00), 2), "stock": random.randint(0, 100), "tags": [
            random_string(15, 2),
            random_string(10, 1),
            random_string(20, 3),
        ], "brand": "test brand", "sku": random_sku(), "weight": round(random.uniform(0.10, 10.00), 2), "dimensions": {
            "width": round(random.uniform(10, 300.00), 2),
            "height": round(random.uniform(10, 300.00), 2),
            "depth": round(random.uniform(10, 300.00), 2)
        }, "warrantyInformation": "1 month warranty", "shippingInformation": "Ships in 1 month",
                           "availabilityStatus": "Low Stock", "reviews": [
            {
                "rating": round(random.uniform(0.00, 5.00), 2),
                "comment": random_string(250, 30),
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "reviewerName": random_string(20, 2),
                "reviewerEmail": random_email()
            },
            {
                "rating": round(random.uniform(0.00, 5.00), 2),
                "comment": random_string(60, 10),
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "reviewerName": random_string(17, 2),
                "reviewerEmail": random_email()
            }
        ], "returnPolicy": "30 days return policy", "minimumOrderQuantity": random.randint(1, 100), "meta": {
            "barcode": "9164035109868",
            "qrCode": "..."
        }, "thumbnail": "...", "images": []}

def build_product_payload(category, **overrides):
    payload = copy.deepcopy(BASE_PRODUCT_PAYLOAD)
    payload["category"] = category
    payload.update(overrides)
    return payload


