from django.shortcuts import render
from django.contrib.auth.backends import ModelBackend, get_user_model
from django.db.models import Q
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .serializers import MSMSerializer
from rest_framework import mixins
from .models import VerifyCode

# Create your views here.

User = get_user_model()


# 短信验证,并且要把验证码保存到数据库
class SmsCodeViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    # 序列化器，和表单类似有验证功能
    serializer_class = MSMSerializer
    queryset = VerifyCode.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CustomModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            print(e)
            return None
