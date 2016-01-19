from discount import mixins
from discount.models import DiscountBase


class PercentDiscount(DiscountBase, mixins.PercentDiscountMixin):
    pass

    #class Meta:
        #app_label = 'discount'


class CartItemPercentDiscount(DiscountBase, mixins.CartItemPercentDiscountMixin):
    pass

    #class Meta:
        #app_label = 'discount'


class CartItemAbsoluteDiscount(DiscountBase, mixins.CartItemAbsoluteDiscountMixin):
    pass

    #class Meta:
        #app_label = 'discount'
