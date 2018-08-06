from rest_framework import serializers
from .models import Goods, GoodsCategory


class GoodsCategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        # 把所有的属性都用上的写法
        fields = "__all__"


class GoodsCategorySerializer2(serializers.ModelSerializer):
    # 子目录，在models中related_name = "sub_cat"
    sub_cat = GoodsCategorySerializer3(many=True)

    class Meta:
        model = GoodsCategory
        # 把所有的属性都用上的写法
        fields = "__all__"


# 商品类别序列化期
class GoodsCategorySerializer(serializers.ModelSerializer):
    sub_cat = GoodsCategorySerializer2(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


# 商品序列化期
class GoodsSerializer(serializers.ModelSerializer):
    category = GoodsCategorySerializer()

    class Meta:
        model = Goods
        fields = "__all__"
