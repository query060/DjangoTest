import xadmin
from .models import UserFav,UserLeavingMessage,UserAddress


class UserFavAdmin(object):
    list_display=["user","goods","add_time"]


class UserLeavingMessageAdmin(object):
    list_display = ['user', 'msg_type', "message", "add_time"]

class UserAddressAdmin(object):
    list_display = ["signing_name", "signing_mobile", "district", "address"]



xadmin.site.register(UserFav,UserFavAdmin)
xadmin.site.register(UserAddress, UserAddressAdmin)
xadmin.site.register(UserLeavingMessage, UserLeavingMessageAdmin)


