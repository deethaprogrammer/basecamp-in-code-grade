class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price
    
    def get_price(self, amount):
        if amount < 10:
            price = self.price * amount
        elif 10 <= amount < 99:
            price = (self.price * 0.9) * amount
        else:
            price = (self.price * 0.8) * amount
        return int(price)
    
    def make_purchase(self, amount):
        self.amount -= amount