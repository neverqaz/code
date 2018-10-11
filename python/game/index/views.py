from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from .models import *
from .send import *
import datetime
# Create your views here.

# url(r'^about/$', views.about),
#     url(r'^contact/$', views.contact),
#     url(r'^gallery/$', views.gallery),
#     url(r'^singlepost/$', views.singlepost),

def index(request):
    article = Article.objects.all()
    return render(request, 'index.html', {'article': article})

def about(request):
    return render(request,'about.html')

# def contact(request):
#     return render(request,'contact.html')
class Contact(View):
    def get(self,request):
        return render(request,'contact.html')
    def post(self,request):
        password=str(request.POST.get('password'))
        name=str(request.POST.get('name'))
        email=str(request.POST.get('email'))
        title=str(request.POST.get('title'))
        contact=str(request.POST.get('message'))
        send(name,email,password,contact,title)
        return HttpResponse('<script>alert("发送成功");location.href="/contact/"</script>')
def gallery(request):
    return render(request,'http://pubg.lihailezzc.com/zhanji')

def single(request):
    return render(request, 'single.html')
class Index(View):
    def get(self,request):
        article=Article.objects.all()
        return render(request,'index.html',{'article':article})
    def post(self,request):
        article=Article.objects.all()
        return render(request,'index.html',{'article':article})
