from django.views.generic.base import View
#from django.views.generic import ListView
from goods.models import Goods
class GoodsListView(View):
    def get(self,request):
        """

        通过django的view实现商品的列表页
        :param request:
        :return:
        """
        json_list=[]
        goods=Goods.objects.all()[:10]
        # for good in goods:
        #     json_dict={}
        #     json_dict["name"]=good.name
        #     json_dict["category"]=good.category
        #     json_dict["market_price"]=good.market_price
        #     json_list.append(json_dict)


        #
        # from django.forms.models import model_to_dict
        # for good in goods:
        #     json_dict=model_to_dict(good)
        #     json_list.append(json_dict)
        # from django.http import HttpResponse
        # import json
        # return HttpResponse(json.dumps(json_list), content_type="application/json")
        import json
        from django.core import serializers
        json_data=serializers.serialize("json",goods)
        json_data=json.loads(json_data)

        from django.http import HttpResponse,JsonResponse

        # return HttpResponse(json.dumps(json_data),content_type="application/json")
        return JsonResponse(json_data,safe=False)














