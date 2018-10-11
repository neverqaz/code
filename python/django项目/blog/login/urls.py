from django.conf.urls import url,include

from login import views
urlpatterns = [
   #url(r'$',views.login),
    url(r'login/$',views.Login.as_view()),
    url(r'register/$',views.Register.as_view()),
    url(r'main/$',views.Login.as_view())

]