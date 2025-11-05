inventory = {
    "(id start with p and end with 3 digits)": {
        "name": "name of the product",
        "category": "product type",
        "price": "price of the product",
        "stock": "amount of items that are in stock",
        "variants": {
            "color=silver": 2 #amount of a variant of the product. inventory json has examples
        }
    }
}
"""
application:

---menu---
[A] Add a new product
[U] Update an existing product
[D] Delete an existing product
[Q] Quit the program

what the code needs to do:
ask for:
> Input product ID:
> Input product name:
> Input product category:
> Input product price:
> Do you want to enter a variant (yes/no)?
yes
> Enter variant name:
> Enter variant stock level:
> Do you want to enter a variant (yes/no)?
no
> Product added!

what is given:
a function that reads the inventory.json

You should print the result of every action. For example, if adding the product worked, you should print: Product added!.
Likewise, if adding the product failed for example because the ID already exists, you should print: Product ID already exists.

For updating you should ask for product id, price and variants in the same way as adding.
You could only update existing products.
You are also not allowed to add new categories.
When added succesfull print Product updated! and when you can not update show ID doesn't exist

With delete you ask for product id. 
If you could delete print Product deleted! when failed because id doesn't exist print `ID doesn't exist.


"""
# Functions to implement
# You will implement the following functions:

def add_product(inventory: dict, product_id: str, name: str, category: str, price: float, stock: int, variants: dict) -> bool:
	"""
	Adds a product to the given inventory.
	Ensures the product ID is unique.
	Returns `True` if the product was successfully added, `False` otherwise.
	"""
def update_product(inventory: dict, product_id: str, price: float = None, variant: dict = None) -> bool:
	"""
    Updates an existing product's price and/or variant stock and total stock.
	Ensures the product exists.
	Ensures the variants exist.
	Ensures the total stock matches the sum of the variants stock.
	Returns `True` if the product was successfully updated, `False` otherwise.
    """
# Keep in mind that updating a variant stock must also change the total stock.
# Also, updating a product can only update existing variants and must not allow creating new variants.

def delete_product(inventory: dict, product_id: str) -> bool:
	"""
	Removes a product from the inventory.
	Ensures the product exists.
	Returns `True` if the product was successfully deleted from the inventory, `False` otherwise.
	"""
# Unit tests
# You are expected to write unit tests for the functions you have implemented,
# you will get an extra point for this. You could write the code first,
# or you could also choose to first write the unit tests as the function signatures (what parameters it expects and what it will return) are already given.