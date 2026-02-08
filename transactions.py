import random
import json
from datetime import datetime
import uuid
from decimal import Decimal

def generate_transaction(item, itemcode, quantity, price, total, payment_type):
    data = {
        "id": str(uuid.uuid4()),
        "timestamp":datetime.now().isoformat(),
        "item":item,
        "itemcode":itemcode,
        "quantity":quantity,
        "price": str(price),
        "total": str(total),
        "payment_type": payment_type
    }
    return data

itemnames = ["Acme T-shirt", "Acme Fleece Jacket", "Acme Chino Shorts"]
itemprices = [
    Decimal("29.90"),
    Decimal("49.90"),
    Decimal("39.90")
]

def generate_itemcode():
    return random.randint(400000, 499999)

def generate_quantity():
    return random.randint(1, 11)

def generate_payment_type():
    return random.choice(["Credit Card", "Cash"])

test_transactions = []

for _ in range(100):
    idx = random.randint(0, len(itemnames) -1)
    item = itemnames[idx]
    itemcode = generate_itemcode()
    price = itemprices[idx]
    quantity = int(generate_quantity())
    total = price * quantity
    payment_type = generate_payment_type()
    test_transactions.append(generate_transaction(item, itemcode, quantity, price, total, payment_type))

with open("transactions.json", "w") as file:
    json.dump(test_transactions, file, indent=2)