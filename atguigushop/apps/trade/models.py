from django.db import models

from users.models import UserProfile
#from django.contrib.auth import get_user_model
from goods.models import Goods
from datetime import datetime

# Create your models here.
#User=get_user_model()

class ShopingCart(models.Model):
    user=models.ForeignKey(UserProfile,verbose_name="用户")
    goods=models.ForeignKey(Goods,verbose_name="商品")
    goods_nums=models.IntegerField(default=0,verbose_name="商品数量")
    add_time=models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name = "购物车"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s(%s)".format(self.goods.name,self.goods_nums)


class OrderInfo(models.Model):
    # 订单状态：单词变大写或者小写：ctr+shift+u
    ORDER_STATUS = (
        ("PAYING", "待支付"),
        ("TRADE_SUCESS", "支付成功"),
        ("TRADE_CLOSE", "支付关闭"),
        ("TRADE_FAIL", "支付失败"),
        ("TRADE_FINSHED", "交易结束"),
    )


    user=models.ForeignKey(UserProfile,verbose_name="用户")
    order_sn=models.CharField(max_length=30,unique=True,verbose_name="订单号")
    trade_sn=models.CharField(max_length=100,unique=True,blank=True,null=True,verbose_name="交易号")
    pay_status=models.CharField(default="PAYING",max_length=30,choices=ORDER_STATUS,verbose_name="订单状态")
    order_message=models.CharField(max_length=200,blank=True,null=True,verbose_name="订单留言",help_text="订单留言")
    order_amount=models.FloatField(default=0.0,verbose_name="订单金额")
    pay_time=models.DateTimeField(null=True,blank=True,verbose_name="支付时间")
    signing_name=models.CharField(max_length=30,verbose_name="签收人")
    signing_mobile=models.CharField(max_length=11,verbose_name="联系电话")
    address=models.CharField(max_length=200,verbose_name="收货地址")
    add_time=models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name = "订单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order_sn)


class OrderGoods(models.Model):
    order=models.ForeignKey(OrderInfo,verbose_name="订单",related_name="goods")
    goods=models.ForeignKey(Goods,verbose_name="商品")
    goods_nums=models.IntegerField(default=0,verbose_name="商品数量")
    add_time=models.DateTimeField(default=datetime.now,verbose_name="添加时间")


    class Meta:
        verbose_name = "订单商品详情"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order.order_sn)
