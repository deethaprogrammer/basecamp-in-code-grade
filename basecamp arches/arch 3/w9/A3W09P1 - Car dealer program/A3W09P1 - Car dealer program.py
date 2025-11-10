class Car:
    def __init__(self, brand, model, color, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
        self.sold = False
        self.sold_to = False

    def sell(self, Customer=None):
        self.sold = True
        self.sold_to = Customer

    def print(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Price: {self.price}")
        if self.sold_to:
            print("Sold to:", self.sold_to.name)
        else:
            print("Not sold")


class Customer:
    def __init__(self, name):
        self.name = name


    def print(self):
        print(self.name)


class Motorcycle:
    def __init__(self, brand, model, color, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
        self.sold = False
        self.sold_to = False

    def sell(self, Customer=None):
        self.sold = True
        self.sold_to = Customer

    def print(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Price: {self.price}")
        if self.sold_to:
            print("Sold to:", self.sold_to.name)
        else:
            print("Not sold")


if __name__ == "__main__":
    pass