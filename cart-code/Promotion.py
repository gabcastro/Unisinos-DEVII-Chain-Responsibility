from IPromotion import Promotion
from lib.Cart import Cart

class NonePromotion(Promotion):
    def handlerDiscount(self, cart: Cart):
        return cart.value


class PromotionNumItems(Promotion):
    def __init__(self, next=None):
        self.next = next

    def handlerDiscount(self, cart: Cart):
        if len(cart.items) >= 5:
            return cart.value - (cart.value * 0.1)

        return self.next.handlerDiscount(cart)


class PromotionInValue(Promotion):
    def __init__(self, next=None):
        self.next = next

    def handlerDiscount(self, cart: Cart):
        if cart.value >= 1_000:
            return cart.value - (cart.value * 0.2)

        return self.next.handlerDiscount(cart)
        
        
class PromotionSelected:
    def handlerDiscount(self, value):
        return PromotionInValue(
            next=PromotionNumItems(next=NonePromotion())
        ).handlerDiscount(value)