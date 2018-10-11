"""paotui1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken import views
from django.contrib import admin
from apps.orders.views import OrderSendListViewSet,OrderAcceptViewset
from apps.userprofile.views import UserViewSet
from apps.user_operation.views import UserAddressViewset,LeavingMessageViewset,UserAliViewset\
    ,SendOrderUserAliPayViewset,AlipayView\
    ,AlipaySystemOrderSettleViewset,\
    AlipaySystemOrderRefundViewset,MapReturn
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import settings
from django.views.static import serve
# from apps.userprofile.views import AliLogin
router = DefaultRouter()
router.register(r'accept_order',OrderAcceptViewset,base_name="accept_order")

router.register(r'send_user_alipay',SendOrderUserAliPayViewset,base_name='send_user_alipay')

router.register(r'sendorders', OrderSendListViewSet,base_name='sendorders')
router.register(r'users', UserViewSet,base_name='users')
router.register(r'address',UserAddressViewset,base_name='address')
router.register(r'messages',LeavingMessageViewset,base_name='messages')
router.register(r'system/accept_user/settle',AlipaySystemOrderSettleViewset,base_name='settle')
router.register(r'system/send_user/refund',AlipaySystemOrderRefundViewset,base_name='refund')

#登录支付宝信息
router.register(r'ali_login',UserAliViewset,base_name="ali")
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^",include(router.urls)),
    url(r'^docs/', include_docs_urls(title='校园跑腿接口文档')),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api-token-auth/', views.obtain_auth_token),
    #url(r'^ali_login/',AliLogin.as_view())
    url("baidu/",TemplateView.as_view(template_name="baidu.html"),name="baidu"),
    url('alipay/return/', AlipayView.as_view(),name="alipay"),
    url('map_return/',MapReturn.as_view(),name="map_return")
    , url("index/",TemplateView.as_view(template_name="index.html"),name="index"),
url('^static/',serve, {'document_root':settings.STATIC_ROOT}),
    url('^media/',serve, {'document_root':settings.MEDIA_ROOT})

]