from lib.Cart import Cart
from lib.Product import Product
import Promotion

cart = Cart()
cart.add_product(Product(product='Snack', value=2))

promo = Promotion.PromotionSelected()

print(f'Value before try apply a promotion: {cart.value}')
print(f'Value after try apply a promotion: {promo.handlerDiscount(cart)}')