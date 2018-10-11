from django.shortcuts import render

# Create your views here.
from apps.user_operation.models import AlipayOrderSettle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import permissions
from utils.permission import IsOwnerOrReadOnly
from rest_framework import viewsets
from utils.baidumaps import BAIDUMAPS
from .models import Order,OrderAccept
from .serializers import OrderSendSerializer,OrderAcceptSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from apps.userprofile.models import Users
from rest_framework import mixins
from apps.user_operation.models import UserAddress
from utils.miaodiyun import MiaoDiYun
class OrderPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    page_query_param="page"
    max_page_size = 100
class OrderSendListViewSet(viewsets.ModelViewSet):
    #RetrieveModelMixin是商品详情页
    """
     获取订单列表页
    """

    serializer_class = OrderSendSerializer
    pagination_class=OrderPagination
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    #filter_class=GoodsFilter
    filter_fields = ('order_type', 'order_emergency',"is_accept")
    search_fields=('name','id')
    ordering_fields = ('order_total', 'tax')


    def get_permissions(self):
        if self.action == "list":
            return [permissions.IsAuthenticated()]  # 用户查看不需要权限
        else:
            return [permissions.IsAuthenticated()]
    def get_queryset(self):
        if self.action=="list" or self.action=="retrieve":
            return Order.objects.get_queryset().order_by('id')

        else:

            return Order.objects.filter(currentuser=self.request.user)
    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        send_users = Users.objects.filter(id=self.request.user.id)
        check_address=UserAddress.objects.filter(id=self.request.data["currentaddress"])
        if send_users:
            address=check_address.values("address")[0]["address"]
            for send_user in send_users:
                serializer.validated_data["send_user_id"] = send_user.id
                serializer.validated_data["send_name"] = send_user.name
                serializer.validated_data["send_mobile"] = send_user.mobile
                serializer.validated_data["send_address"]=address
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

class OrderAcceptViewset(mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,viewsets.GenericViewSet):
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = OrderAcceptSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        accept_order=self.perform_create(serializer)
        orderac_id=self.request.data["orderac"]
        addressac_id=self.request.data["addressac"]
        check_order=Order.objects.filter(id=orderac_id)
        check_accept_address=UserAddress.objects.filter(id=addressac_id)
        send_address_id=check_order.values("currentaddress")[0]["currentaddress"]
        check_send_address=UserAddress.objects.filter(id=send_address_id)
        if check_order and check_accept_address and check_send_address:
            accept_address_point=check_accept_address.values("address_point")[0]["address_point"]
            accept_address= check_accept_address.values("address")[0]["address"]
            send_address_point=check_send_address.values("address_point")[0]["address_point"]
            accept_address_city=check_accept_address.values("city")[0]["city"]
            #send_address_city=check_send_address.values("city")[0]["city"]
           # if accept_address_city==send_address_city:#城市相同
            result1=BAIDUMAPS().calulation_distance(origin=send_address_point,destination=accept_address_point,mode="walking",region=accept_address_city)
            distance = result1.get("distance", "")
            run_money = result1.get("run_money", "")
            tax = result1.get("tax", "")
            #dict2 = {"distance": distance, "duration": duration, "run_money": run_money, "tax": tax}
            # else:#城市不相同
            #     distance=0
            #     run_money=0
            #     tax=0
            purchase=check_order.values("purchase")[0]["purchase"]
            order_total=purchase+tax+run_money
            is_accept=list(check_order.values("is_accept"))[0]["is_accept"]
            send_user_id=check_order.values("send_user_id")[0]["send_user_id"]
            if is_accept==False:
                check_order.update(is_accept=True,accept_user_id=self.request.user.id,accept_name=self.request.user.name,accept_mobile=self.request.user.mobile,order_total=order_total,distance=distance,run_money=run_money,tax=tax,accept_address=accept_address)

            #1.通知发单用户付钱(待测试项)
            # send_mobile=query1.get("send_mobile","")
            # accept_name=query1.get("accept_name","")
            # send_name=query1.get("send_name","")
            # if send_name!=None and accept_name!=None and send_mobile!=None:
            #     miaodiyun=MiaoDiYun()
            #     miaodiyun.send_message(send_mobile,send_name,accept_name)
            #2.订单结算时把发单用户的id和order_id放到结算表里
            check_alipay_order_settle=AlipayOrderSettle.objects.filter(order_id=orderac_id,useraos_id=send_user_id)
            if check_alipay_order_settle.count()==0:
                check_alipay_order_settle.create(order_id=orderac_id,useraos_id=send_user_id)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        #id=list(Order.objects.filter(send_user_id__exact=self.request.user).values("id"))[0]["id"]#设置接单不显示自己的订单
        return OrderAccept.objects.filter(useroac=self.request.user)
