from rest_framework import viewsets
from rest_framework import authentication
from .serializers import UsersSerializer,UserRegisterSerializer
from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_encode_handler,jwt_payload_handler
from rest_framework.response import Response
from rest_framework import status
from .models import Users

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    authentication_classes = (authentication.SessionAuthentication, JSONWebTokenAuthentication)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UsersSerializer
        elif self.action == "create":
            return UserRegisterSerializer

        return UsersSerializer

    def get_permissions(self):
        if self.action == 'retrieve':
            return [permissions.IsAuthenticated()]
        elif self.action == "create":
            return []  # 用户创建不需要权限
        elif self.action=="update":
            return [permissions.IsAuthenticated()]
        elif self.action=="delete":
            return [permissions.IsAuthenticated()]

        return []
    #
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
    def get_queryset(self):
        if self.action=="list":
           return Users.objects.filter(id=self.request.user.id)
        else:
            return Users.objects.get_queryset().order_by('id')
