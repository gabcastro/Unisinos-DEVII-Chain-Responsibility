class Product:
    def __init__(self, product: str, value: int):
        self.product = product
        self.value = value

    def __repr__(self):
        return f'Product(product={self.product}, value={self.value})'