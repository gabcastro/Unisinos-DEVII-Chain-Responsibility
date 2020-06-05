from lib.Cart import Cart
from lib.Product import Product
import Promotion

cart = Cart()

cart.add_product(Product(product='Smartphone', value=1_200))
cart.add_product(Product(product='Sunglasses', value=800))

promo = Promotion.PromotionSelected()

print(f'Value before try apply a promotion: {cart.value}')
print(f'Value after try apply a promotion: {promo.handlerDiscount(cart)}')