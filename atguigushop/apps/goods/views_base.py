from django.views.generic import View
from django.core import serializers
from django.http import HttpResponse,JsonResponse
import json
from goods.models import Goods



class GoodsListView(View):
    def get(self, request):
        goods_list = Goods.objects.all()[:10]
        # json_list = []
        # print(goods_list)
        # for goods in goods_list:
        #     json_item = {}
        #     json_item["name"] = goods.name
        #     json_item["market_price"] = goods.market_price
        #     json_item["sold_num"] = goods.sold_num
        #
        #     json_list.append(json_item)
        #
        # print(type(json_list))
        # content=json.dumps(json_list)
        # print(type(content))
        data=serializers.serialize("json",goods_list)

        data=json.loads(data)

        return JsonResponse(data,safe=False)




