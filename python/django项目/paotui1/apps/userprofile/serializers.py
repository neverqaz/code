from .models import Users
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth import get_user_model
import re
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from paotui1.settings import REGEX_MOBILE,REGEX_EMAIL,REGEX_CARD
from utils.aliusers import get_alipay_user
from .models import Users
# Create your views here.
class CustomBackend(ModelBackend):
    '''
    自定义登录方式

    '''
    def authenticate(self, request, username=None, password=None, **kwargs):
          try:
            user=Users.objects.get(Q(username=username)|Q(mobile=username)|Q(email=username))
            if user.check_password(password):
                return user
          except Exception as e:
              return None
class UsersSerializer(serializers.ModelSerializer):
    ali_user_url = serializers.SerializerMethodField(read_only=True)

    def get_ali_user_url(self, obj):
        url=get_alipay_user()
        return url
    class Meta:
        model = Users
        fields = ["name", "gender", "email", "compus_card", "mobile","id",'ali_user_url']
class UserRegisterSerializer(serializers.ModelSerializer):
    name=serializers.CharField(required=True,allow_blank=True,
                                   validators=[UniqueValidator(queryset=Users.objects.all(),message="用户已经存在")]
                                   , label="用户名")
    mobile=serializers.CharField(max_length=11,label="手机号码")
    email=serializers.CharField(required=True,label="邮箱")
    compus_card=serializers.CharField(max_length=13,label="校园卡号")
    id=serializers.IntegerField(read_only=True)
    password = serializers.CharField(required=True, style={'input_type': 'password'}, label="密码", write_only=True)

    def validate_mobile(self, mobile):
        """
        验证手机号码
        :param data:
        :return:
        """
        # 手机是否注册
        if Users.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError('电话号码已被注册')

        # 验证手机号码是否存在
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError('手机号码不合法')
        return mobile
    def validate_email(self, email):
        """
        验证手机号码
        :param data:
        :return:
        """
        # 手机是否注册
        if Users.objects.filter(email=email).count():
            raise serializers.ValidationError('邮箱已被注册')

        # 验证手机号码是否存在
        if not re.match(REGEX_EMAIL, email):
            raise serializers.ValidationError('邮箱不合法')
        return email
    def validate_compus_card(self,compus_card):
        """
        验证手机号码
        :param data:
        :return:
        """
        # 手机是否注册
        if Users.objects.filter(compus_card=compus_card).count():
            raise serializers.ValidationError('校园卡已被注册')

        # 验证手机号码是否存在
        if not re.match(REGEX_CARD, compus_card):
            raise serializers.ValidationError('校园卡不合法')
        return compus_card
    def validate(self, attrs):#attrs是经过所有字段验证之后所传过来的字段字典
        attrs["username"]=attrs["mobile"]
        return attrs
    class Meta:
        model=Users
        fields=["name","gender","email","compus_card","id","password","mobile","birthday"]

    