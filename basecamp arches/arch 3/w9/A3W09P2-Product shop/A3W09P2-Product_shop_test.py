from Product_shop import Product


def test_normal_amount_get_price():
    p = Product("Item 1", 10, 5)
    price = p.get_price(5)
    assert price == 25


def test_discount_10_percent_get_price():
    p = Product("Item 1", 10, 5)
    price = p.get_price(10)
    assert price == 45


def test_discount_20_percent_get_price():
    p = Product("Item 1", 10, 5)
    price = p.get_price(100)
    assert price == 400


def test_normal_amount_make_purchase():
    p = Product("Item 1", 10, 5)
    p.make_purchase(5)
    assert p.amount == 5

test_normal_amount_get_price()
test_discount_10_percent_get_price()
test_discount_20_percent_get_price()
test_normal_amount_make_purchase()