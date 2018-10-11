from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from .models import UserFav,UserLeavingMessage,UserAddress
from .serializers import UserFavSerializer,UserFavDetailSerializer,UserAddressSerializer
from rest_framework.permissions import IsAuthenticated
from utils.permission import IsOwnerOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication

# Create your views here.
class UserFavViewset(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    list:
         获取用户收藏列表
    retrieve:
             判断某个商品是否收藏
    create:
          收藏商品
    destroy:
           删除商品


    """
    #queryset =UserFav.objects.all()
    permission_classes = (IsAuthenticated,IsOwnerOrReadOnly)
    #serializer_class = UserFavSerializer
    authentication_classes = (JSONWebTokenAuthentication,SessionAuthentication)
    lookup_field = "goods_id"
    def get_queryset(self):
        return UserFav.objects.filter(user=self.request.user)#获取当前用户的所收藏的商品

    def get_serializer_class(self):
        if self.action == 'list':
            return UserFavDetailSerializer
        elif self.action == "create":
            return UserFavSerializer

        return UserFavSerializer
    # def perform_create(self, serializer):
    #     instance=serializer.save()
    #     goods=instance.goods
    #     goods.fav_num+=1
    #     goods.save()
from .serializers import LeavingMessageSerializer
class LeavingMessageViewset(mixins.ListModelMixin,mixins.DestroyModelMixin,
                            mixins.CreateModelMixin,viewsets.GenericViewSet):
    """
    list:
        获取用户留言
    create:
          添加留言
    delete：
           删除留言

    """
    serializer_class = LeavingMessageSerializer
    permission_classes = (IsAuthenticated,IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication,SessionAuthentication)
    def get_queryset(self):
        return UserLeavingMessage.objects.filter(user=self.request.user)

"""class UserAddressViewset(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):"""
class UserAddressViewset(viewsets.ModelViewSet):
    """
    收货地址管理
    list:
         获取收货地址列表
    create:
          添加收货地址
    destroy:
          删除收货地址
    update:
          修改收货地址
    """
    serializer_class = UserAddressSerializer
    permission_classes = (IsAuthenticated,IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication,SessionAuthentication)
    def get_queryset(self):
        return UserAddress.objects.filter(user=self.request.user)


