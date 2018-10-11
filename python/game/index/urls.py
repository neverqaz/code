from django.conf.urls import url,include
from django.contrib.staticfiles.urls import static,settings
from index import views
urlpatterns = [
    url(r'^$', views.Index.as_view(),name='index'),
    #url(r'$',views.index),
    url(r'^about/$', views.about,name='about'),
    url(r'^contact/$', views.Contact.as_view()),
    url(r'^gallery/$', views.gallery),
    url(r'^ueditor/',include('DjangoUeditor.urls' )),
    ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)