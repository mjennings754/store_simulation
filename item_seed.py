from item import Item, save_items
import random

def random_itemcode():
    return random.randint(400000, 499999)

items = [
    Item("Men", 31, random_itemcode(), "Acme Fleece Jacket", "25FW", "Fleece", 49.90, False, False, stock=194)
]

save_items(items)