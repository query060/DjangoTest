from django.db import models
from datetime import datetime
from DjangoUeditor.models import UEditorField


# Create your models here.


class GoodsCategory(models.Model):
    CATEGORY_TYPE = (
        (1, "一级类目"),
        (2, "二级类目"),
        (3, "三级类目"),
    )
    name = models.CharField(default="", max_length=20, verbose_name="类目名称", help_text="类目名称")
    code = models.CharField(default="", max_length=30, null=True, blank=True, verbose_name="编码code")
    desc = models.TextField(default="", max_length=30, null=True, blank=True, verbose_name="类目描述", help_text="类目描述")
    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="类目级别", help_text="类目级别", null=True, blank=True)
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="父类目", help_text="父类目",related_name="sub_cat")
    is_tab = models.BooleanField(default=False, verbose_name="是否导航", help_text="是否导航")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsCategoryBrand(models.Model):
    category = models.ForeignKey(GoodsCategory, related_name="brands", null=True, blank=True, verbose_name="商品类目")
    name = models.CharField(default="", max_length=30, verbose_name="品牌名称", help_text="品牌名称")
    desc = models.CharField(default="", max_length=100, verbose_name="品牌描述", help_text="品牌描述")
    image = models.ImageField(max_length=200, upload_to="brands/images/")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        ##重载meta模块,修改Admin后台中显示的名称
        verbose_name = "品牌名"
        verbose_name_plural = verbose_name
        # 自定义表名
        db_table = "goods_goodsbrand"

    def __str__(self):
        return self.name


class Goods(models.Model):
    # 商品类目
    category = models.ForeignKey(GoodsCategory, verbose_name="商品类目", help_text="商品类目")

    goods_sn = models.CharField(max_length=50, default="", verbose_name="商品唯一货号", help_text="商品唯一货号")
    name = models.CharField(max_length=100, verbose_name="商品名称", help_text="商品名称")
    click_num = models.IntegerField(default=0, verbose_name="点击数", help_text="点击数")
    sold_num = models.IntegerField(default=0, verbose_name="销售量", help_text="销售量")
    fav_num = models.IntegerField(default=0, verbose_name="收藏数", help_text="收藏数")
    goods_num = models.IntegerField(default=0, verbose_name="库存数", help_text="库存数")
    market_price = models.FloatField(default=0.0, verbose_name="市场价格", help_text="市场价格")
    shop_price = models.FloatField(default=0.0, verbose_name="本店价格", help_text="本店价格")
    goods_brief = models.TextField(max_length=500, verbose_name="商品简明描述", help_text="商品简明描述")
    ship_free = models.BooleanField(default=True, verbose_name="是否承担运费", help_text="是否承担运费")
    goods_front_image = models.ImageField(upload_to="goods/images/", null=True, blank=True, verbose_name="封面图")
    is_new = models.BooleanField(default=False, verbose_name="是否新品")
    is_hot = models.BooleanField(default=False, verbose_name="是否热销")
    goods_desc = UEditorField('内容', width=1000, height=300, imagePath="goods/images/", filePath="goods/files/",default="")

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsImage(models.Model):
    goods = models.ForeignKey(Goods, verbose_name="商品轮播图", related_name="images")
    image = models.ImageField(upload_to="", verbose_name="图片", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品图片"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class Banner(models.Model):
    goods = models.ForeignKey(Goods, verbose_name="商品")
    image = models.ImageField(upload_to="banner", verbose_name="轮播图片")
    index = models.IntegerField(default=0, verbose_name="轮播顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "轮播商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name