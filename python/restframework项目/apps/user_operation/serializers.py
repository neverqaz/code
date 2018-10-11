from rest_framework import serializers
from .models import UserFav,UserAddress
from rest_framework.validators import UniqueTogetherValidator
from goods.serializer import GoodsSerializer
class UserFavDetailSerializer(serializers.ModelSerializer):
    goods=GoodsSerializer()
    class Meta:
        model=UserFav
        fields = ('goods', 'id')
class UserFavSerializer(serializers.ModelSerializer):
    user= serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model=UserFav
        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=('user', 'goods')
                ,message="已经收藏"
            )
        ]
        fields=('user','goods','id')
from .models import UserLeavingMessage
class LeavingMessageSerializer(serializers.ModelSerializer):
     user=serializers.HiddenField(default=serializers.CurrentUserDefault())
     add_time=serializers.DateTimeField(read_only=True,format="%Y-%m-%d %H:%M:%s")
     class Meta:
         model=UserLeavingMessage
         fields=("user","msg_type","subject","message","file","id","add_time")

class UserAddressSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model=UserAddress
        fields=('signer_name',"province","city",'district','address','signer_mobile','id','user')