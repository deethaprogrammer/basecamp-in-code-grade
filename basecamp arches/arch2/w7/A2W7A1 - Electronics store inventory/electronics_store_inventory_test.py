import pytest
from electronics_store_inventory import get_inventory, add_product, update_product, delete_product

def test_add_product_duplicate():
    inventory = get_inventory()
    variants = {"color=silver": 3,
            "color=black": 2}
    result1 = add_product(inventory, "P001", "Laptop X200", "Laptop", 1299.99, 5, variants)
    assert result1 is False
    
    result2 = add_product(inventory, "P051", "Laptop X200", "Laptop", 1299.99, 5, variants)
    assert result2 is True


def test_update_product():
    inventory = get_inventory()
    variants = {"color=silver": 7,
            "color=black": 4}
    result1 = update_product(inventory, "P001", 300, variants)
    assert result1 is True
    result2 = update_product(inventory, "P991", 300, variants)
    assert result2 is False

def test_delete_product():
    inventory = get_inventory()
    result1 = delete_product(inventory, "P001")
    assert result1 is True
    result2 = delete_product(inventory, "P050")
    assert result2 is False