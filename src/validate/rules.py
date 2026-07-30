REQUIRED_COLUMNS = {
    "customers": [
        "customer_id",
        "customer_unique_id",
    ],

    "orders": [
        "order_id",
        "customer_id",
        "order_purchase_timestamp",
    ],

    "order_items": [
        "order_id",
        "product_id",
        "seller_id",
        "price",
    ],

    "payments": [
        "order_id",
        "payment_value",
    ],

    "reviews": [
        "review_id",
        "order_id",
    ],

    "products": [
        "product_id",
    ],

    "sellers": [
        "seller_id",
    ],
}

