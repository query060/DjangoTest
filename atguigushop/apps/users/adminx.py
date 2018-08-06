from xadmin import views
import xadmin
from .models import VerifyCode



class GlobalSettings(object):
    site_title="硅谷商品后台"
    site_footer="atguigu_shop"



class VerifyCodeAdmin(object):

    list_display=['code','mobile','add_time']



xadmin.site.register(VerifyCode,VerifyCodeAdmin)
xadmin.site.register(views.CommAdminView,GlobalSettings)