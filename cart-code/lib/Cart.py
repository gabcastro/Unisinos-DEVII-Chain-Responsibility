from lib.Product import Product

class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, item: Product):
        self.items.append(item)

    @property
    def value(self):
        return sum(map(lambda item: item.value, self.items))