from item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super function to have access to all parents attributes/method
        super().__init__(name, price, quantity)

        assert (
            broken_phones >= 0
        ), f"Broken Phones{broken_phones} is not greater or equal 0 !"

        self.broken_phones = broken_phones

    def __repr__(self):
        return super().__repr__()[:-1] + f", {self.broken_phones})"
