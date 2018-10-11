from django.conf.urls import url,include
from single import views
urlpatterns = [


    #url(r'^about/$', views.about,name='about'),
    # url(r'^contact/$', views.contact),
    # url(r'^gallery/$', views.gallery),
    url(r'^$', views.Single.as_view()),
     url(r'^form/$',views.form)]