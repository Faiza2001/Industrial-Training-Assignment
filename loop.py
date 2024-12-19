# Assignment 1: Create a script that processes a dictionary of products, checking stock levels and generating restock alerts if necessary.
products = {
    "laptop": {"stock": 4, "min_required": 10},
    "smartphone": {"stock": 15, "min_required": 5}
}

# Function to check stock levels and generate restock alerts
def check_stock(products):
    for product, details in products.items():
        stock = details["stock"]
        min_required = details["min_required"]

        if stock < min_required:
            print(f"Alert: {product.capitalize()} needs restocking. Current stock: {stock}, Minimum required: {min_required}.")
        else:
            print(f"{product.capitalize()} has sufficient stock. Current stock: {stock}, Minimum required: {min_required}.")

check_stock(products)
