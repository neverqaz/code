from django.shortcuts import render
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.mixins import CreateModelMixin
from rest_framework import mixins
from rest_framework import viewsets
from .serializers import SmsSerializer,UserRegisterSerializer,UserDetailSerializer
from rest_framework.response import Response
from rest_framework import status
from utils.yunpian import YunPian
from Mxshop.settings import APIKEY
from random import choice
from .models import VerifyCode
from rest_framework_jwt.serializers import jwt_encode_handler,jwt_payload_handler

User=get_user_model()
# Create your views here.
class CustomBackend(ModelBackend):
    '''
    自定义登录方式

    '''
    def authenticate(self, request, username=None, password=None, **kwargs):
          try:
            user=User.objects.get(Q(username=username)|Q(mobile=username))
            if user.check_password(password):
                return user
          except Exception as e:
              return None


class SmsCodeViewset(CreateModelMixin,viewsets.GenericViewSet):
    """
    发送短信验证码
    """
    serializer_class = SmsSerializer

    def generate_code(self):
        """
        生成四位数字的验证码
        :return:
        """
        seeds="1234567890"
        random_str=[]
        for i in range(4):
            random_str.append(choice(seeds))
        return "".join(random_str)#数组变字符串




    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mobile=serializer.validated_data['mobile']
        yun_pain=YunPian(APIKEY)
        code = self.generate_code()
        sms_status=yun_pain.send_sms(code=code,mobile=mobile)
        if sms_status['code']!=0:
            """
            通过返回的状态码判断是否成功
            """
            return Response({
                "mobile":sms_status["msg"]

            },status=status.HTTP_400_BAD_REQUEST)
        else:
            code_record=VerifyCode(code=code,mobile=mobile)#在短信发送成功之后保存到数据库
            code_record.save()
            return Response({
                "mobile":mobile
            },status=status.HTTP_201_CREATED)
from rest_framework import permissions
from rest_framework import authentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from utils.permission import IsOwnerOrReadOnly
class UserViewset(CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):
    """
    用户的创建是不需要权限的，而用户的查看详情详情信息和修改是必须登录之后才能操作
    """
    #serializer_class = UserRegisterSerializer
    queryset = User.objects.all()
    #permission_classes = (IsAuthenticated,IsOwnerOrReadOnly)
    authentication_classes = (authentication.SessionAuthentication,JSONWebTokenAuthentication)

    def get_serializer_class(self):
        if self.action=='retrieve':
            return UserDetailSerializer
        elif self.action=="create":
            return UserRegisterSerializer

        return UserDetailSerializer


    def get_permissions(self):
        if self.action=='retrieve':
            return [permissions.IsAuthenticated()]
        elif self.action=="create":
            return []#用户创建不需要权限

        return []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=self.perform_create(serializer)
        """
        生成jwt的token
        """
        re_dict=serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"]=jwt_encode_handler(payload)
        re_dict["name"]=user.name if user.name else user.username


        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()
    def get_object(self):#RetrieveModelMixin当中的方法
        return self.request.user


