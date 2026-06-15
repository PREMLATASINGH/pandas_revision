import pandas as pd
import random
try:
    from faker import Faker
    fake = Faker()
except Exception:
    fake = None
    # Minimal fallback for environments without the `faker` package
    from datetime import date, timedelta
    _FIRST_NAMES = ["James","Mary","John","Patricia","Robert","Jennifer","Michael","Linda","William","Elizabeth"]
    _LAST_NAMES = ["Smith","Johnson","Williams","Brown","Jones","Miller","Davis","Garcia","Rodriguez","Wilson"]
    def _fallback_name():
        return f"{random.choice(_FIRST_NAMES)} {random.choice(_LAST_NAMES)}"
    def _fallback_date_between(start_date="-1y", end_date="today"):
        # support the same semantic range used by Faker: last year to today
        end = date.today()
        start = end - timedelta(days=365)
        delta = (end - start).days
        return start + timedelta(days=random.randint(0, delta))

products = [
    ("Wireless Mouse", "Electronics", 19.99),
    ("Keyboard", "Electronics", 24.99),
    ("LED Monitor", "Electronics", 129.99),
    ("Smartwatch", "Electronics", 149.99),
    ("Coffee Maker", "Home Appliances", 79.99),
    ("Hair Dryer", "Home Appliances", 29.99),
    ("Blender", "Home Appliances", 49.99),
    ("Running Shoes", "Fashion", 59.99),
    ("Backpack", "Fashion", 39.99),
    ("Perfume", "Fashion", 29.99),
    ("Office Chair", "Furniture", 89.99),
    ("Table Lamp", "Home Decor", 14.99),
    ("Wall Clock", "Home Decor", 19.99),
    ("Cricket Bat", "Sports", 79.99),
    ("Water Bottle", "Sports", 9.99),
    ("Notebook Pack", "Stationery", 3.99),
    ("Desk Organizer", "Stationery", 7.99),
    ("USB Cable", "Electronics", 5.99),
    ("Wireless Earbuds", "Electronics", 49.99),
    ("Treadmill", "Sports", 399.99)
]

payment_methods = ["Credit Card", "Debit Card", "Cash", "UPI"]
cities = ["Edison", "Iselin", "Newark", "Jersey City", "Woodbridge"]

rows = []

for i in range(5000):
    customer_id = f"C{str(i+1).zfill(4)}"
    order_id = f"O{10001+i}"
    if fake:
        order_date = fake.date_between(start_date="-1y", end_date="today")
        name = fake.name()
    else:
        order_date = _fallback_date_between(start_date="-1y", end_date="today")
        name = _fallback_name()
    city = random.choice(cities)
    product, category, price = random.choice(products)
    quantity = random.randint(1, 5)
    total = round(price * quantity, 2)
    payment = random.choice(payment_methods)

    rows.append([
        customer_id, order_id, order_date, name, city,
        product, category, quantity, price, total, payment
    ])

df = pd.DataFrame(rows, columns=[
    "customer_id","order_id","order_date","customer_name","city",
    "product","category","quantity","price","total_amount","payment_method"
])

df.to_csv("customer_sales_5000.csv", index=False)
print("Dataset created: customer_sales_5000.csv")
df=pd.read_csv("customer_sales_5000.csv")
print(df.head())
