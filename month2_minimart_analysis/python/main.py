# Entry point for the MiniMart data reporting system
new_orders = [
    {"order_id": 6, "customer_id": 1, "product_id": 2, "quantity": 5, "order_date": "2023-06-06"},
    {"order_id": 7, "customer_id": 3, "product_id": 3, "quantity": 2, "order_date": "2023-06-07"},
    {"order_id": 8, "customer_id": 4, "product_id": 1, "quantity": 3, "order_date": "2023-06-08"}
]

# Sample prices
product_prices = {
    1: 1.50,  # Cola
    2: 2.00,  # Pounded Yam
    3: 3.50,  # Suya
    4: 2.75,  # Akamu
    5: 2.25   # Palm Wine
}

# Flaging large orders
def flag_large_orders(orders, prices):
    for order in orders:
        total = prices[order["product_id"]] * order["quantity"]
        if total > 100:
            print(f"Order {order['order_id']} (Customer {order['customer_id']}) is a large order with total ${total:.2f}")

flag_large_orders(new_orders, product_prices)

# Converting to eur and applying discounts
exchange_rate = 0.85  # USD to EUR
discounted_orders = []
for order in new_orders:
    price = product_prices[order["product_id"]]
    quantity = order["quantity"]
    total_usd = price * quantity
    total_eur = total_usd * exchange_rate
    discount = 0.10 if quantity > 3 else 0  # 10% discount for quantity > 3
    final_total_eur = total_eur * (1 - discount)
    discounted_orders.append({
        "order_id": order["order_id"],
        "customer_id": order["customer_id"],
        "total_eur": final_total_eur,
        "discount_applied": discount * 100 if discount > 0 else 0
    })

for order in discounted_orders:
    print(f"Order {order['order_id']} Total: {order['total_eur']:.2f} EUR, Discount: {order['discount_applied']}%")

# Combine original and new orders
all_orders = [
    {"customer_id": 1, "product_id": 1, "quantity": 2},
    {"customer_id": 2, "product_id": 2, "quantity": 3},
    {"customer_id": 1, "product_id": 3, "quantity": 1},
    {"customer_id": 3, "product_id": 4, "quantity": 4},
    {"customer_id": 4, "product_id": 5, "quantity": 2},
    *[{k: v for k, v in order.items() if k in ["customer_id", "product_id", "quantity"]} for order in new_orders]
]

from collections import defaultdict

total_products_sold = sum(order["quantity"] for order in all_orders)
product_counts = defaultdict(int)
for order in all_orders:
    product_counts[order["product_id"]] += order["quantity"]
most_popular_product = max(product_counts.items(), key=lambda x: x[1])[0]
revenue_per_customer = defaultdict(float)
for order in all_orders:
    revenue_per_customer[order["customer_id"]] += product_prices[order["product_id"]] * order["quantity"]

report = {
    "total_products_sold": total_products_sold,
    "most_popular_product": most_popular_product,
    "revenue_per_customer": dict(revenue_per_customer)
}

print("Report:", report)

# Save to JSON and print formatted summary
import json
with open("report.json", "w") as f:
    json.dump(report, f, indent=4)

print("\nFormatted Summary:")
print(f"Total Products Sold: {report['total_products_sold']}")
print(f"Most Popular Product ID: {report['most_popular_product']}")
for customer_id, revenue in report["revenue_per_customer"].items():
    print(f"Revenue for Customer {customer_id}: ${revenue:.2f}")
