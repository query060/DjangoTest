from .models import Goods, GoodsCategory, GoodsCategoryBrand, GoodsImage, Banner
import xadmin


class GoodsAdmin(object):
    list_display = ["name", "click_num", "fav_num", "goods_num", "market_price", "shop_price", "goods_desc", "is_hot",
                    "add_time"]
    search_fields = ["name"]
    style_fields = {"goods_desc": "ueditor"}


class GoodsCategoryAdmin(object):
    list_display = ["name", "code", "category_type", "parent_category", "add_time"]
    list_filter = ["category_type", "parent_category", "name"]
    search_fields = ['name']


class GoodsCategoryBrandAdmin(object):
    list_display = ["category", "image", "name", "desc"]


class GoodsImageAdmin(object):
    pass


class BannerAdmin(object):
    pass


xadmin.site.register(Goods, GoodsAdmin)
xadmin.site.register(GoodsCategory, GoodsCategoryAdmin)
xadmin.site.register(GoodsCategoryBrand, GoodsCategoryBrandAdmin)
xadmin.site.register(GoodsImage, GoodsImageAdmin)
xadmin.site.register(Banner, BannerAdmin)
