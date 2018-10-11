from rest_framework import serializers
from .models import Order,OrderAccept
from apps.user_operation.models import UserAddress
import time
from apps.user_operation.serializers import UserAddressSerializer
from utils.baidumaps import BAIDUMAPS
class OrderSendSerializer(serializers.ModelSerializer):
    currentuser= serializers.HiddenField(default=serializers.CurrentUserDefault())
    order_status=serializers.IntegerField(read_only=True)
    order_sn=serializers.CharField(read_only=True)
    run_money=serializers.FloatField(read_only=True)
    tax=serializers.FloatField(read_only=True)
    order_status=serializers.IntegerField(read_only=True)
    order_pay_status=serializers.CharField(read_only=True)
    is_accept =serializers.BooleanField(read_only=True)
    order_total=serializers.FloatField(read_only=True)
    distance=serializers.FloatField(read_only=True)
    add_time = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%s")
    send_user_id=serializers.IntegerField(read_only=True)
    accept_user_id = serializers.IntegerField(read_only=True)
    accept_address = serializers.CharField(read_only=True)
    accept_name = serializers.CharField(read_only=True)
    accept_mobile = serializers.CharField(read_only=True)
    send_name = serializers.CharField(read_only=True)
    send_mobile = serializers.CharField(read_only=True)
    send_address=serializers.CharField(read_only=True)
    pay_time=serializers.DateTimeField(read_only=True)
    add_time = serializers.DateTimeField(read_only=True)
    def generate_order_sn(self):
        # 生成订单号order_sn：当前时间+userid+随机数
        from random import Random
        random_ins = Random()
        order_sn = "{time_str}{userid}{random_str}".format(time_str=time.strftime("%Y%m%d%H%M%S"),
                                                           userid=self.context["request"].user.id,
                                                           random_str=random_ins.randint(10, 99))
        return order_sn



    def validate(self, attrs):
        attrs["order_sn"]=self.generate_order_sn()
        return attrs
    class Meta:
        model = Order
        fields = "__all__"

class OrderAcceptSerializer1(serializers.ModelSerializer):
    currentuser= serializers.HiddenField(default=serializers.CurrentUserDefault())
    order_status=serializers.IntegerField(read_only=True)
    order_sn=serializers.CharField(read_only=True)
    run_money=serializers.FloatField(read_only=True)
    tax=serializers.FloatField(read_only=True)
    order_status=serializers.IntegerField(read_only=True)
    order_pay_status=serializers.CharField(read_only=True)
    order_total=serializers.FloatField(read_only=True)
    distance=serializers.FloatField(read_only=True)
    add_time = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%s")
    send_user_id=serializers.IntegerField(read_only=True)
    accept_user_id = serializers.IntegerField(read_only=True)
    send_name = serializers.CharField(read_only=True)
    send_mobile = serializers.CharField(read_only=True)

    class Meta:
        model = Order
        fields = "__all__"

class OrderAcceptSerializer(serializers.ModelSerializer):
    useroac = serializers.HiddenField(default=serializers.CurrentUserDefault())
    gps_navigation_url = serializers.SerializerMethodField(read_only=True)
    orderac=serializers.PrimaryKeyRelatedField(required=True,queryset=Order.objects.filter(is_accept=False))
    addressac=serializers.PrimaryKeyRelatedField(required=True,queryset=UserAddress.objects.all())
    def get_gps_navigation_url(self, obj):
        check_accept_address = UserAddress.objects.filter(id=obj.addressac_id, useraddr=obj.useroac_id)
        check_order=Order.objects.filter(id=obj.orderac_id,accept_user_id=obj.useroac_id)
        send_address = check_order.values("send_address")[0]["send_address"]
        send_user_id=int(check_order.values("send_user_id")[0]["send_user_id"])
        check_send_address = UserAddress.objects.filter(address=send_address, useraddr=send_user_id)
        if check_send_address.count() > 0 and check_accept_address.count() > 0 and check_order.count()>0:
            send_address_point = check_send_address.values("address_point")[0]["address_point"]
            accept_address_point = check_accept_address.values("address_point")[0]["address_point"]
            accept_address=check_accept_address.values("address")[0]["address"]
            send_address=check_order.values("send_address")[0]["send_address"]
            return BAIDUMAPS().gps_follow(origin=accept_address_point,
                                          origin_name=accept_address,
                                          destination=send_address_point,
                                          destination_name=send_address,
                                          mode="walking",region=obj.addressac.city)
        else:
            return ""
    class Meta:
        model = OrderAccept
        fields = "__all__"
