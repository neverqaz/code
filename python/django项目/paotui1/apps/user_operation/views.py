from django.shortcuts import render

# Create your views here.
from rest_framework import mixins,viewsets
from .serializers import LeavingMessageSerializer,UserAddressSerializer,UserAliSerializer,AlipayOrderSettleSerializer,AlipaySystemOrderSettleSerializer
from rest_framework.permissions import IsAuthenticated
from utils.permission import IsOwnerOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from .models import UserLeavingMessage,UserAddress,UserAli,AlipayOrderSettle
from rest_framework.response import Response
from utils.ali_auth_token import Ali_AUTH_TOKEN
from paotui1.settings import private_key_path,ali_pub_key_path
import requests
from apps.orders.models import Order
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
        return UserLeavingMessage.objects.filter(userlm=self.request.user)

"""class UserAddressViewset(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):"""
class UserAddressViewset(mixins.ListModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
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
        return UserAddress.objects.filter(useraddr=self.request.user)
class UserAliViewset(mixins.ListModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):
    """
    支付宝账户信息
    list:
         获取支付宝账户列表


    update:

    """
    serializer_class = UserAliSerializer
    permission_classes = (IsAuthenticated,IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication,SessionAuthentication)
    auth_code=''
    def get_queryset(self):
        return UserAli.objects.filter(usera=self.request.user)
    def list(self, request, *args, **kwargs):
        auth_code = request.GET.get("auth_code", '')
        ali_users=UserAli.objects.filter(usera_id=self.request.user.id)
        if auth_code!=""and ali_users.count()==0:
                ali_user = Ali_AUTH_TOKEN(
                    appid="2016091700530193",
                    app_private_key_path=private_key_path,
                    alipay_public_key_path=ali_pub_key_path,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
                    debug=True,  # 默认False,
                )
                url = ali_user.direct_auth(auth_code)
                re_url = "https://openapi.alipaydev.com/gateway.do?{data}".format(data=url)
                #x=requests.get(re_url).json()#.encode("utf-8").decode('unicode_escape')
                access_token = requests.get(re_url).json()["alipay_system_oauth_token_response"]["access_token"]
                url1 = ali_user.direct_user(access_token)
                re_url = "https://openapi.alipaydev.com/gateway.do?{data}".format(data=url1)
                user = requests.get(re_url).json()
                avatar = user["alipay_user_info_share_response"]["avatar"] if user["alipay_user_info_share_response"].keys()=="avatar" else ""
                nick_name = user["alipay_user_info_share_response"]["nick_name"] if user["alipay_user_info_share_response"].keys()=="nick_name" else ""
                userali_id =user["alipay_user_info_share_response"]["user_id"]
                query1=UserAli.objects.filter(userali_id=userali_id)
                if userali_id!=None and query1.count()==0:
                    UserAli.objects.create(usera_id=self.request.user.id, nick_name=nick_name,
                                       avatar=avatar,
                                       userali_id=userali_id)
                else:
                    ali_users.update(nick_name=nick_name,
                                       avatar=avatar,
                                       userali_id=userali_id)
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)

            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
class SendOrderUserAliPayViewset(mixins.ListModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):
    serializer_class = AlipayOrderSettleSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    def get_queryset(self):
        return AlipayOrderSettle.objects.filter(useraos=self.request.user)
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        check_order = Order.objects.filter(currentuser=self.request.user, is_accept=True,
                                           send_user_id=self.request.user.id)
        check_send_ali_user = UserAli.objects.filter(usera=self.request.user)
        if check_order.count()>0 and check_send_ali_user.count()>0:
            order_accpet_user = list(check_order.values("accept_user_id"))[0]["accept_user_id"]
            if order_accpet_user != None:
                check_accept_ali_user = UserAli.objects.filter(usera=order_accpet_user)
                if check_order.count() > 0 and check_send_ali_user.count() > 0 and check_accept_ali_user.count() > 0:
                    amount = list(check_order.values("order_total"))[0]["order_total"]
                    send_order_user = list(check_send_ali_user.values("userali_id"))[0]["userali_id"]
                    order_sn = list(check_order.values("order_sn"))[0]["order_sn"]
                    accept_order_user = list(check_accept_ali_user.values("userali_id"))[0]["userali_id"]
                    AlipayOrderSettle.objects.filter(useraos=self.request.user).update(trans_out=send_order_user,
                                                                                 trans_in=accept_order_user,amount=amount,
                                                                                   out_trade_no=order_sn)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
class AlipaySystemOrderSettleViewset(mixins.ListModelMixin,viewsets.GenericViewSet):
    serializer_class = AlipaySystemOrderSettleSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    def get_queryset(self):
        return AlipayOrderSettle.objects.filter(useraos=self.request.user)
    def generate_ordersettle_sn(self):
        # 生成结算号：当前时间+userid+随机数
        import time
        from random import Random
        random_ins = Random()
        ordersettle_sn = "{time_str}{userid}{random_str}34".format(time_str=time.strftime("%Y%m%d%H%M%S"),
                                                           userid=self.request.user.id,
                                                           random_str=random_ins.randint(10, 99))
        return ordersettle_sn
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        check_order = Order.objects.filter(currentuser=self.request.user, is_accept=True,
                                           send_user_id=self.request.user.id)
        if check_order.count()>0:
            for d in check_order:
                #一旦点击该接口首先订单状态改为完成态“1”
                d.order_status=1
                d.save()
            order_id=list(check_order.values("id"))[0]["id"]
            check_alipaysettle=AlipayOrderSettle.objects.filter(useraos=self.request.user,order_id=order_id)
            if check_alipaysettle.count()>0:
                for c in check_alipaysettle:
                    c.out_request_no=self.generate_ordersettle_sn()
                    c.save()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
class AlipaySystemOrderRefundViewset(mixins.ListModelMixin,viewsets.GenericViewSet):
    """
    退款
    list：退款
    """
    serializer_class = AlipaySystemOrderSettleSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    def get_queryset(self):
        return AlipayOrderSettle.objects.filter(useraos=self.request.user)


from rest_framework.views import APIView
from datetime import datetime
from utils.alipay import AliPay
from rest_framework.response import Response
from django.shortcuts import redirect
class AlipayView(APIView):
    def get(self,request):
        """
        处理支付宝的return_url的返回
        :param request:
        :return:
        """
        processed_dict = {}
        for key, value in request.GET.items():
            processed_dict[key] = value
        sign = processed_dict.pop("sign", None)

        alipay = AliPay(
            appid="2016091700530193",
            app_notify_url="http://123.206.43.75:8082/alipay/return/",
            app_private_key_path=private_key_path,
            alipay_public_key_path=ali_pub_key_path,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            debug=True,  # 默认False,
            return_url="http://123.206.43.75:8082/alipay/return/"
        )
        verify_re = alipay.verify(processed_dict, sign)
        if verify_re is True:
            order_sn = processed_dict.get("out_trade_no", None)
            trade_no = processed_dict.get('trade_no', None)
            #trade_status = processed_dict.get("trade_status", None)
            existed_orders = Order.objects.filter(order_sn=order_sn)
            for existed_order in existed_orders:
                existed_order.order_pay_status = "TRADE_SUCCESS"
                existed_order.pay_time = datetime.now()
                existed_order.order_status=2
                existed_order.save()
            #支付宝交易号：trade_sn
            existed_alipaysettleds=AlipayOrderSettle.objects.filter(out_trade_no=order_sn)
            for existed_alipaysettled in existed_alipaysettleds:
                existed_alipaysettled.alipay_trade_no=trade_no
                existed_alipaysettled.save()
            #return Response("success")
            response=redirect("index")
            response.set_cookie("nextPath","pay",max_age=2)#俩秒
            return response
        else:
            response = redirect("index")
            return response


    def post(self,request):
        """
        处理支付宝的notify_url
        :param request:
        :return:
        """
        processed_dict = {}
        for key, value in request.GET.items():
            processed_dict[key] = value
        sign = processed_dict.pop("sign", None)

        alipay = AliPay(
            appid="2016091700530193",
            app_notify_url="http://123.206.43.75:8082/alipay/return/",
            app_private_key_path=private_key_path,
            alipay_public_key_path=ali_pub_key_path,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            debug=True,  # 默认False,
            return_url="http://123.206.43.75:8082/alipay/return/"
        )
        verify_re = alipay.verify(processed_dict, sign)
        if verify_re is True:
            order_sn = processed_dict("out_trade_no", None)
            trade_no = processed_dict('trade_no', None)
            trade_status = processed_dict("trade_status", None)
            existed_orders = Order.objects.filter(order_sn=order_sn)
            for existed_order in existed_orders:
                existed_order.order_pay_status = trade_status
                existed_order.pay_time = datetime.now()
                existed_order.order_status = 2
                existed_order.save()
            # 支付宝交易号：trade_sn
            existed_alipaysettleds = AlipayOrderSettle.objects.filter(out_trade_no=order_sn)
            for existed_alipaysettled in existed_alipaysettleds:
                existed_alipaysettled.alipay_trade_no = trade_no
                existed_alipaysettled.save()
            # return Response("success")
            response = redirect("index")
            response.set_cookie("nextPath", "pay", max_age=2)  # 俩秒
            return response
        else:
            response = redirect("index")
            return response
class MapReturn(APIView):
    def get(self,request):
        point=request.GET.get("point")
        address=request.GET.get("address")
        city=request.GET.get("city")
        check_address=UserAddress.objects.filter(useraddr=request.user)
        check_address.create(useraddr=request.user,address_point=point,address=address,user_mobile=request.user.mobile,user_name=request.user.name,city=city)
        return redirect("index")
