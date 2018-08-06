import os
import sys

filename = os.path.realpath(__file__)
print(filename)

dirname = os.path.dirname(filename)
print(dirname)

sys.path.insert(0, dirname)
print(sys.path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "atguigushop.settings")

import django

django.setup()

from db_utils.data.product_data import row_data

from goods.models import Goods, GoodsCategory, GoodsImage

for item in row_data:
    goods = Goods()
    goods.market_price = float(item["market_price"].replace("元", "").replace("￥", ""))
    goods.shop_price = float(item["market_price"].replace("元", "").replace("￥", ""))
    goods.name = item["name"] if item["name"] is not None else ""
    # 商品的简单描述
    goods.goods_brief = item["desc"] if item["desc"] is not None else ""
    # 商品的详细描述
    goods.goods_desc = item["goods_desc"] if item["goods_desc"] else ""

    goods.goods_front_image=item["images"][0] if item["images"] else ""

    # 类目：三级类目或者二级类目
    category_name = item["categorys"][-1]
    # 查看类目是否存在
    categorys = GoodsCategory.objects.filter(name=category_name)
    # print("categorys===",categorys)

    if categorys:
        goods.category = categorys[0]

    goods.save()

    for image in item["images"]:
        goods_image = GoodsImage()
        goods_image.image = image
        goods_image.goods = goods

        goods_image.save()
