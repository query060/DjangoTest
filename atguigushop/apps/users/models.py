from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.

class UserProfile(AbstractUser):
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名",help_text="姓名")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月",help_text="出生年月")
    gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女')), default='female',verbose_name="性别",help_text="性别")
    mobile = models.CharField(max_length=11, verbose_name="手机号码",help_text="手机号码")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱",help_text="邮箱")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = "用户信息"

    def __str__(self):
        return self.username




class VerifyCode(models.Model):
    code=models.CharField(max_length=4,verbose_name="验证码",help_text="验证码")
    mobile=models.CharField(max_length=11,verbose_name="手机号码",help_text="手机号码")
    add_time=models.DateTimeField(default=datetime.now,verbose_name="添加时间",help_text="添加时间")

    class Meta:
        verbose_name = "验证码"
        verbose_name_plural = "验证码"

    def __str__(self):
        return self.code
