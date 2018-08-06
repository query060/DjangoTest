from .models import ShopingCart,OrderInfo,OrderGoods
import xadmin

class ShopingCartAdmin(object):
    list_display=["user","goods","goods_nums"]


class OrderInfoAdmin(object):
    pass

class OrderGoodsAdmin(object):
    pass


xadmin.site.register(ShopingCart,ShopingCartAdmin)
xadmin.site.register(OrderInfo,OrderInfoAdmin)
xadmin.site.register(OrderGoods,OrderGoodsAdmin)
