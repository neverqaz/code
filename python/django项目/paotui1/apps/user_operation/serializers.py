from .models import UserLeavingMessage,UserAddress,UserAli,AlipayOrderSettle
from rest_framework import serializers
from apps.orders.models import Order
from utils.alipay import AliPay
from paotui1.settings import private_key_path,ali_pub_key_path
class LeavingMessageSerializer(serializers.ModelSerializer):
     userlm=serializers.HiddenField(default=serializers.CurrentUserDefault())
     add_time=serializers.DateTimeField(read_only=True,format="%Y-%m-%d %H:%M:%s")
     class Meta:
         model=UserLeavingMessage
         fields=("userlm","msg_type","subject","message","file","id","add_time")
class UserAddressSerializer(serializers.ModelSerializer):
    useraddr= serializers.HiddenField(default=serializers.CurrentUserDefault())
    getlocation_url=serializers.SerializerMethodField(read_only=True)
    def get_getlocation_url(self,obj):
        return "http://neverqaz.cn/baidu"
    class Meta:
        model=UserAddress
        fields="__all__"
class UserAliSerializer(serializers.ModelSerializer):
    usera = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model=UserAli
        fields="__all__"

class AlipayOrderSettleSerializer(serializers.ModelSerializer):
    useraos=serializers.HiddenField(default=serializers.CurrentUserDefault())
    alipay_url=serializers.SerializerMethodField(read_only=True)
    order_id = serializers.IntegerField(read_only=True)
    out_request_no = serializers.CharField(read_only=True)
    trans_out = serializers.CharField(read_only=True)
    trans_in = serializers.CharField(read_only=True)
    amount = serializers.FloatField(read_only=True)
    add_time=serializers.DateTimeField(read_only=True)
    def get_alipay_url(self,obj):
                alipay = AliPay(
                    appid="2016091700530193",
                    app_notify_url="http://123.206.43.75:8082/alipay/return/",
                    app_private_key_path=private_key_path,
                    alipay_public_key_path=ali_pub_key_path,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
                    debug=True,  # 默认False,
                    return_url="http://123.206.43.75:8082/alipay/return/"
                )

                url = alipay.direct_pay(
                    subject="跑腿网",
                    out_trade_no=obj.out_trade_no,
                    total_amount=obj.amount
                )
                re_url = "https://openapi.alipaydev.com/gateway.do?{data}".format(data=url)
                return re_url

    class Meta:
        model=AlipayOrderSettle
        fields="__all__"
class AlipaySystemOrderSettleSerializer(serializers.ModelSerializer):
    useraos = serializers.HiddenField(default=serializers.CurrentUserDefault())
    alisettle_url = serializers.SerializerMethodField(read_only=True)

    def get_alisettle_url(self, obj):
        alipay = AliPay(
            appid="2016091700530193",
            app_notify_url="http://123.206.43.75:8082/index/",
            app_private_key_path=private_key_path,
            alipay_public_key_path=ali_pub_key_path,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            debug=True,  # 默认False,
            return_url="http://123.206.43.75:8082/index/"
        )
        #out_request_no, trade_no, trans_out, trans_in, amount
        url = alipay.direct_settle(
            out_request_no=obj.out_request_no,
            trade_no=obj.alipay_trade_no,
            trans_out="2088102175995850",#跑腿网收钱的账户
            trans_in=obj.trans_in,
            amount=obj.amount)
        re_url = "https://openapi.alipaydev.com/gateway.do?{data}".format(data=url)
        return re_url
    class Meta:
        model=AlipayOrderSettle
        fields="__all__"
class AlipaySystemOrderRefundSerializer(serializers.ModelSerializer):
    """
    退款
    """
    useraos = serializers.HiddenField(default=serializers.CurrentUserDefault())
    alirefund_url = serializers.SerializerMethodField(read_only=True)

    def get_alipay_url(self, obj):
        alipay = AliPay(
            appid="2016091700530193",
            app_notify_url="http://123.206.43.75:8082/alipay/return/",
            app_private_key_path=private_key_path,
            alipay_public_key_path=ali_pub_key_path,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            debug=True,  # 默认False,
            return_url="http://123.206.43.75:8082/alipay/return/"
        )
        #out_request_no, trade_no, trans_out, trans_in, amount
        url = alipay.direct_refund(
            trade_no=obj.alipay_trade_no,
            amount=obj.amount)
        re_url = "https://openapi.alipaydev.com/gateway.do?{data}".format(data=url)
        return re_url
    class Meta:
        model=AlipayOrderSettle
        fields="__all__"