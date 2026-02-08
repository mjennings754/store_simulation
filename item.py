import random
import json
from pathlib import Path
DATA_FILE = Path("items.json")

def generate_itemcode():
    return random.randint(400000, 499999)

class Item:
    def __init__(self, department, division, itemcode, name, season, material, price, limited_offer, sale, stock):
        self.department = department
        self.division = division
        self.itemcode = itemcode
        self.name = name
        self.season = season
        self.material = material
        self.price = price
        self.limited_offer = limited_offer
        self.sale = sale
        self.stock = stock

    def json(self):
        return {
            "department": self.department,
            "division": self.division,
            "itemcode": self.itemcode,
            "name": self.name,
            "season": self.season,
            "material": self.material,
            "price": self.price,
            "limited_offer": self.limited_offer,
            "sale": self.sale,
            "stock": self.stock
        }
    
    @classmethod
    def from_json(cls, data):
        return cls(**data)
    
def save_items(items):
    with open('items.json', 'w') as f:
        json.dump([item.json() for item in items], f, indent=2)

def load_items():
    if not DATA_FILE.exists():
        return []
    
    with open(DATA_FILE) as f:
        data = json.load(f)

    return [Item.from_json(d) for d in data]