from django.shortcuts import render
from .serializer import GoodsSerializer,CategorySerializer,BannerSerializer,IndexCategorySerialiizer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from rest_framework import status
from .models import Goods,Banner
from rest_framework import mixins
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle
from rest_framework import viewsets
from .filters import GoodsFilter
# class GoodsListView(APIView):
#     """
#     List all goods.
#     """
#     def get(self, request, format=None):
#         goods = Goods.objects.all()#[:10]
#         goods_serializer = GoodsSerializer(goods, many=True)
#         return Response(goods_serializer.data)
#
#     def post(self, request, format=None):
#         serializer = GoodsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class GoodsListView(mixins.ListModelMixin,generics.GenericAPIView):
#     """
#     商品列表页
#     """
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
class GoodsPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param="page"
    max_page_size = 100



# class GoodsListView(generics.ListAPIView):
#     """
#     商品列表页,分页，搜索，过滤，排序
#     """
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#     pagination_class=GoodsPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
class GoodsListViewSet(CacheResponseMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    #RetrieveModelMixin是商品详情页
    """
    商品列表页
    """
    throttle_classes = (UserRateThrottle,AnonRateThrottle)
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class=GoodsPagination
    #authentication_classes = (TokenAuthentication,)需要登录认证的加上
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_class=GoodsFilter
    #filter_fields = ('name', 'shop_price')
    search_fields=('^name','goods_brief','goods_desc')
    ordering_fields = ('sold_num', 'shop_price')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_num+=1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
'''
'^'开始 - 搜索。
'='完全匹配。
'@'全文搜索。（目前只支持Django的MySQL后端。）
'$'正则表达式搜索。
例如：

search_fields = ('=username', '=email')'''
#     过滤
#     def get_queryset(self):
    #     queryset=Goods.objects.all()
    #     price_min=self.request.query_params.get("price_min",0)
    #     if price_min:
    #           queryset=Goods.objects.filter(shop_price__gt=int(price_min))
    #     return queryset


          #return Goods.objects.filter(shop_price_gt=100)
from .models import GoodsCategory
class CategoryViewset(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    '''
    RetrieveModelMixin:
                      列表详情页
    List:
        商品分类列表数据
    '''
    queryset =GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer

class BannerViewset(mixins.ListModelMixin,viewsets.GenericViewSet):
    """
    获取轮播图列表
    """
    queryset = Banner.objects.all().order_by("index")
    serializer_class = BannerSerializer


class IndexCategoryViewset(mixins.ListModelMixin,viewsets.GenericViewSet):
    """
    首页商品分类数据
    """
    queryset = GoodsCategory.objects.filter(is_tab=True,name__in=["生鲜食品","海鲜水产"])#name__in=["生鲜食品","海鲜特产"]
    serializer_class = IndexCategorySerialiizer