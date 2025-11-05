import sys
import os
import json


def get_inventory() -> dict:
    with open(os.path.join(sys.path[0], "inventory.json")) as json_file:
        file_value = json.load(json_file)
        return file_value


def add_product(inventory: dict, product_id: str, name: str, category: str, price: float, stock: int, variants: dict) -> bool:
    """
    Adds a product to the given inventory.
    Ensures the product ID is unique.
    Returns `True` if the product was successfully added, `False` otherwise.
    """
    if not product_id in inventory.keys():
        inventory[product_id] = {}
        inventory[product_id]["name"] = name
        inventory[product_id]["category"] = category
        inventory[product_id]["price"] = price
        inventory[product_id]["stock"] = stock
        if "variants" in variants:
            inventory[product_id]["variants"] = variants["variants"]
        else:
            inventory[product_id]["variants"] = variants
        print(inventory[product_id])
        return True
    return False


def update_product(inventory: dict, product_id: str, price: float = None, variants: dict = None) -> bool:
    """
    Updates an existing product's price and/or variant stock and total stock.
    Ensures the product exists.
    Ensures the variants exist.
    Ensures the total stock matches the sum of the variants stock.
    Returns `True` if the product was successfully updated, `False` otherwise.
    """
    if product_id in inventory.keys():
        inventory[product_id]["price"] = price
        if "variants" in variants:
            inventory[product_id]["variants"] = variants["variants"]
        else:
            inventory[product_id]["variants"] = variants
        if "variants" in variants:
            stock = sum(variants["variants"].values())
        else:
            stock = sum(variants.values())
        inventory[product_id]["stock"] = stock
        print("Product updated")
        return True
    else:
        print("ID doesn't exist")
        return False

def delete_product(inventory: dict, product_id: str) -> bool:
    """
    Removes a product from the inventory.
    Ensures the product exists.
    Returns `True` if the product was successfully deleted from the inventory, `False` otherwise.
    """
    if product_id in inventory.keys():
        inventory.pop(product_id)
        print("product deleted")
        return True
    else:
        print("ID doesn't exist")
        return False


def menu(choice, inventory):
    variant = {"variants": {}}
    if choice == "A":
        product_id = input("Input product ID: ")
        name = input("Input product name: ")
        category = input("Input product category: ")
        price = float(input("Input product price: "))
        while True:
            add_variant = input("Do you want to add a variant (yes/no)?\n>").lower()
            if add_variant == "yes":
                variant_name = input("Enter variant name: ")
                variant_stock = input("Enter variant stock level: ")
                variant["variants"][variant_name] = int(variant_stock)
            elif add_variant == "no":
                break
        stock = sum(variant["variants"].values())
        if add_product(inventory, product_id, name, category, price, stock, variant):
            return print("Product added!")
        else:
            return print("ID already exists")
    if choice == "U":
        product_id = input("Input product ID to update: ")
        price = input("enter the new price: ")
        while input("Do you want to chance\n (yes/no): ") == "yes":
            variant_name = input("Enter variant name: ")
            variant_stock = input("Enter variant stock level: ")
            variant["variants"][variant_name] = int(variant_stock)
        return(update_product(inventory, product_id, price, variant))
    if choice == "D":
        product_id = input("Input the ID of the product that you want to delete")
        return delete_product(inventory, product_id)
    if choice == "Q":
        quit()
    pass


if __name__ == "__main__":
    wrong_input = 0
    inventory = get_inventory()
    while True:
        while wrong_input < 3:
            menu_choice = input("[A] Add a new product\n[U] Update an existing product\n[D] Delete an existing product\n[Q] Quit the program\n>").upper()
            if menu_choice not in ["A", "U", "D", "Q"]:
                print(f'{menu_choice} is not an option in the menu')
                wrong_input +=1
            else:
                break
        if wrong_input == 3:
            quit()
        menu(menu_choice, inventory)