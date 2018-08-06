from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from .models import Goods,GoodsCategory
from .serializers import GoodsSerializer,GoodsCategorySerializer
# from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import filters

from django_filters.rest_framework import DjangoFilterBackend
from .filters import GoodsFilter


# Create your views here.
class GoodsListPagination(PageNumberPagination):
    #默认每页返回10条数据
    page_size = 12
    #自定义数据条数变量
    page_size_query_param = 'size'
    #自定义页数的变量

    page_query_param = 'page'

    max_page_size = 100

class GoodsListView(generics.ListAPIView):
    queryset = Goods.objects.all()
    # 序列化器
    serializer_class = GoodsSerializer

    pagination_class = GoodsListPagination


class GoodsCategoryViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    queryset = GoodsCategory.objects.filter(category_type=1)
    # 序列化器
    serializer_class = GoodsCategorySerializer


class GoodsListViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = Goods.objects.all()
    # 序列化器
    serializer_class = GoodsSerializer
    pagination_class = GoodsListPagination

    filter_backends = (filters.OrderingFilter,filters.SearchFilter, DjangoFilterBackend,)

    filter_class = GoodsFilter
    search_fields=('name','goods_brief','goods_desc')
    ordering_fields=('shop_price','add_time')


