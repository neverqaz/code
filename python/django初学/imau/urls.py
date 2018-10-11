





from django.conf.urls import url,include

urlpatterns = [
   ''' url(r'^admin/', admin.site.urls),
    url(r'^$',views.index),
     url(r'^f/$',views.F.as_view()),
    url(r'^add/(\d+)/(\d+)$',views.index)'''
]