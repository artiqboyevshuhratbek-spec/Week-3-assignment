def place_order(customers_db, menu_catalog, customer_id, item_name, quantity):
    if customer_id not in customers_db:
        raise KeyError("Customer not found")
    if item_name not in menu_catalog:
        raise KeyError("Item not on menu")
    if not isinstance(quantity, int) or quantity < 1:
        raise ValueError("Quantity must be positive integer")
    item_price = menu_catalog[item_name]["price"]
    total_cost = quantity * item_price
    if customers_db[customer_id]["status"] == "Gold":
        total_cost *= 0.9
    if customers_db[customer_id]["wallet"] < total_cost:
        raise ValueError("Insufficient balance")
    customers_db[customer_id]["wallet"] -= total_cost
    return total_cost


def run_delivery_batch(customers_db, menu_catalog, order_list):
    total_sales = 0.0
    failed_orders = 0
    for customer_id, item_name, quantity in order_list:
        try:
            cost = place_order(customers_db, menu_catalog, customer_id, item_name, quantity)
            total_sales += cost
        except Exception as e:
            print(f"Order Failed for {customer_id}: {e}")
            failed_orders += 1

    return {"total_sales": total_sales, "failed_orders": failed_orders}

menu = {
    "Burger": {"price": 10.0},
    "Pizza":  {"price": 15.0}
}

# Format: {ID: {"wallet": float, "status": str}}
customers = {
    "C1": {"wallet": 20.0, "status": "Regular"},
    "C2": {"wallet": 50.0, "status": "Gold"}    # Gets 10% off
}

orders = [
    ("C1", "Burger", 2),    # Valid. Cost: 20.0. Rem: 0.
    ("C2", "Pizza", 4),     # Valid. Cost: (60 * 0.9) = 54. Error: Insufficient balance (50 < 54).
    ("C3", "Salad", 1),     # Error: Customer not found.
    ("C1", "Soda", 1),      # Error: Item not on menu.
    ("C1", "Burger", 0)]
result = run_delivery_batch(customers, menu, orders)
print(result)