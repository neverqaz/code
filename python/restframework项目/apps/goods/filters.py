from rest_framework import generics
from django_filters import rest_framework as filters
from .models import Goods
import django_filters
from django.db.models import Q
class GoodsFilter(filters.FilterSet):
    """
    商品过滤类
    """
    pricemin = filters.NumberFilter(field_name="shop_price", lookup_expr='gte')
    pricemax = filters.NumberFilter(field_name="shop_price", lookup_expr='lte')
    name=filters.CharFilter(field_name='name',lookup_expr='icontains')#忽略大小写
    top_category=filters.NumberFilter(method="top_category_filter")
    def top_category_filter(self,queryset,name,value):
        return queryset.filter(Q(category_id=value)|
                               Q(category__parent_category_id=value)|
                               Q(category__parent_category__parent_category_id=value))

    class Meta:
        model = Goods
        fields = ['pricemin','pricemax','name','top_category','is_hot','is_new']#跟前端对应