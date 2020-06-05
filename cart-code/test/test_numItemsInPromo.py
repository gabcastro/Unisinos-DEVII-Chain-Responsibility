from lib.Cart import Cart
from lib.Product import Product
import Promotion

cart = Cart()

cart.add_product(Product(product='Snack', value=5))
cart.add_product(Product(product='Milk shake', value=20))
cart.add_product(Product(product='Energy drink', value=10))
cart.add_product(Product(product='Water', value=5))
cart.add_product(Product(product='Apple', value=10))

promo = Promotion.PromotionSelected()

print(f'Value before try apply a promotion: {cart.value}')
print(f'Value after try apply a promotion: {promo.handlerDiscount(cart)}')