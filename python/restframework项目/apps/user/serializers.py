from django.contrib.auth import get_user_model
from datetime import datetime
from datetime import timedelta
import re
from rest_framework import serializers
from Mxshop.settings import REGEX_MOBILE
from .models import VerifyCode

User=get_user_model()
class SmsSerializer(serializers.Serializer):
    mobile=serializers.CharField(max_length=11)


    def validate_mobile(self, mobile):
        """
        验证手机号码
        :param data:
        :return:
        """
        #手机是否注册
        if User.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError('用户已经存在')


        #验证手机号码是否存在
        if not re.match(REGEX_MOBILE,mobile):
            raise serializers.ValidationError('手机号码不合法')

        #手机号码验证发送频率(一分钟之前)
        one_mintes_ago=datetime.now()-timedelta(hours=0,minutes=1,seconds=0)
        if VerifyCode.objects.filter(add_time__gt=one_mintes_ago,mobile=mobile).count():
            raise serializers.ValidationError('手机号码发送手机验证码未超过60s')
        return mobile
from rest_framework.validators import UniqueValidator
class UserRegisterSerializer(serializers.ModelSerializer):
    """
    用户序列化
    """
    code=serializers.CharField(required=True,write_only=True,max_length=4,label="验证码",
                               min_length=4,help_text="验证码",
                               error_messages={
                                   "blank":"请输入验证码",
                                   "required":"请输入验证码",
                                   "max_length":"验证码格式错误",
                                   "min_length": "验证码格式错误"

                               })#required=Ture是必填字段
    username=serializers.CharField(required=True,allow_blank=True,
                                   validators=[UniqueValidator(queryset=User.objects.all()
                                                               ,message="用户已经存在")]
                                   , label="用户名")
    password=serializers.CharField(required=True,style={'input_type': 'password'},label="密码",write_only=True)
    def validate_code(self,code):
        """
           用户验证码验证
           """
        verify_records=VerifyCode.objects.filter(mobile=self.initial_data['username']).order_by("-add_time")
        if verify_records:
            last_record=verify_records[0]                        #initial_data['username']是从前端传过来的数据"""

            five_mintes_ago=datetime.now()-timedelta(hours=0,minutes=5,seconds=0)
            if five_mintes_ago>last_record.add_time:
                raise serializers.ValidationError("验证码过期")
            if last_record.code!=code:
                raise serializers.ValidationError("验证码错误")
        else:
            raise serializers.ValidationError("验证码不存在")
        #return code不保存数据库只是验证
    def validate(self, attrs):#attrs是经过所有字段验证之后所传过来的字段字典
        attrs["mobile"]=attrs["username"]
        del attrs["code"]
        return attrs

    # def create(self, validated_data):
    #     """
    #     设置在后台数据库里保存时编码不以明码显示
    #     :param validated_data:
    #     :return:
    #     """
    #     user=super(UserRegisterSerializer,self).create(validated_data=validated_data)
    #     user.set_password(validated_data["password"])
    #     user.save()
    #     return user


    class Meta:
        model=User
        fields=("username","code","mobile","password")


class UserDetailSerializer(serializers.ModelSerializer):
    """
    用户详情序列化
    """
    class Meta:
        model= User
        fields=('name','gender','birthday','email','mobile')





