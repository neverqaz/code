"""Mxshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
import xadmin
from django.urls import path,include
#from  Mxshop.settings import MEDIA_ROOT
from django.contrib.staticfiles.urls import static,settings
from django.views.static import serve
#from goods.views_base import GoodsListView
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from goods.views import  GoodsListViewSet,CategoryViewset,BannerViewset,IndexCategoryViewset
from rest_framework.authtoken import views
from user.views import SmsCodeViewset,UserViewset
from user_operation.views import UserFavViewset,LeavingMessageViewset,UserAddressViewset
from trade.views import ShoppingCartViewset,OrderViewset
'''可选参数：
- base_name:用于创建url的基础名字，如果没有设置，就根据queryset值设置，如果没有设置queryset属性，那么就必须设置base_name. 如果没有设置的话就会报错
'''
router = DefaultRouter()
#配置goods的url
router.register(r'goods', GoodsListViewSet,base_name='goods')
#配置category的url
router.register(r'categorys', CategoryViewset,base_name='categorys')
#配置短信验证码的url
router.register(r'codes', SmsCodeViewset,base_name='codes')

router.register(r'users',UserViewset,base_name='users')
#收藏
router.register(r'userfavs',UserFavViewset,base_name='userfavs')
#用户留言：
router.register(r'messages',LeavingMessageViewset,base_name='messages')
#收货地址
router.register(r'address',UserAddressViewset,base_name='address')
#购物车url
router.register(r'shopcarts',ShoppingCartViewset,base_name='shopcarts')
#订单相关url
router.register(r'orders',OrderViewset,base_name='orders')
#轮播图url
router.register(r'banners',BannerViewset,base_name='banners')
#首页商品系列数据url
router.register(r'indexgoods',IndexCategoryViewset,base_name='indexgoods')



#from goods.views import GoodsListView,

# goods_list = GoodsListViewSet.as_view({
#     'get': 'list',
#     #'post': 'create'
# })
from trade.views import AlipayView
from django.views.generic import TemplateView
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    path('admin/', admin.site.urls),
   # path('media/(?P<path>.*)$',serve,{"document_root":settings.MEDIA_ROOT}),
    # url(r'media/(?P<path>.*)$',serve,{"document_root":MEDIA_ROOT}),
    #商品列表页
    path("",include(router.urls)),
    path("index/",TemplateView.as_view(template_name="index.html"),name="index"),
    path('docs/',include_docs_urls(title='学习rest-framework框架')),
    path('api-auth/', include('rest_framework.urls')),
    #drf 自带的token认证模式
    path('api-token-auth/', views.obtain_auth_token),
    #jwt的认证接口
    path('login/', obtain_jwt_token),
    # url('^docs/', include_docs_urls(title='b'))
    path('alipay/teturn/', AlipayView.as_view(),name="alipay"),
    #第三方登录
    path('', include('social_django.urls', namespace='social')),
    path('static/',serve, {'document_root':settings.STATIC_ROOT}),
    path('media/',serve, {'document_root':settings.MEDIA_ROOT})
#
]
