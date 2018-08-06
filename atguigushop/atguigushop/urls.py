"""atguigushop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
# from django.contrib import admin
import xadmin
from atguigushop.settings import MEDIA_ROOT
# 加载静态资源的服务
from django.views.static import serve
from goods.views import GoodsListViewSet, GoodsCategoryViewSet
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from users.views import SmsCodeViewset

router = DefaultRouter()
router.register(r'goods', GoodsListViewSet)
router.register(r'categorys', GoodsCategoryViewSet)
router.register(r'codes',SmsCodeViewset)

# goods_list=GoodsListViewSet.as_view({
#     'get':'list',
# })

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    # url(r'^goods/$',GoodsListView.as_view(),name='goods_list'),
    # url(r'^goods/$', goods_list, name='goods_list'),

    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'docs/', include_docs_urls(title="硅谷商店")),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
    url(r'^api-token-auth/', views.obtain_auth_token),
    # url(r'^jwt-token-auth/', obtain_jwt_token),
    url(r'^login/', obtain_jwt_token),

]
