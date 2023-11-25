import csv


class Item:
    # The pay rate after 20% discount can be changed'globally' Item.pay_rate = ... it will change
    # pay_rate for all Items or it can be changed by self.pay_rate and it will change pay_rate only
    # for one item
    pay_rate = 0.8

    # Creating a list of all Item Objects
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the recieved arguments
        assert price >= 0, f"Price {price} is not greater or equal to 0 !"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal 0 !"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    ##class method that cam be callable only by Item.instance_from_csv not for instance.
    @classmethod
    def instantiate_from_csv(cls, file):
        path = "C:/Users/Filip/Desktop/Projekty/Python_mini_projects/OOP/" + file
        with open(path, "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get("name"),
                price=float(item.get("price")),
                quantity=float(item.get("quantity")),
            )

    # class that can be equally well be written outside object, but becouse it is connected somehow to a class it is here
    # as a static method

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero (i.e 5.0, 10.0)
        if isinstance(num, float):
            # Is integer is in-bulit function i.e 5,5.0 (True), 5.2 (False)
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return (
            f"{self.__class__.__name__}: ('{self.name}', {self.price}, {self.quantity})"
        )
