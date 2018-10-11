from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from .models import *
# Create your views here.
#def login(request):
 #   return render(request,'login.html')
class  Login(View):

    def post(self,request):
        username=request.POST.get('text',' ')
        password=request.POST.get('password',' ')
        print(username,password)
        print(User.objects.filter(name=username, password=password))
        if User.objects.filter(name=username,password=password).count()!=0:
           # return HttpResponse("验证成功 ，正在进入下一个页面")
            return render(request, 'main.html')
        else:
            return render(request, 'login.html')
    def get(self,request):

        return render(request, 'login.html')
class Register(View):
    def post(self,request):
        username = request.POST.get('text', ' ')
        password = request.POST.get('password', ' ')
        User.objects.create(name=username,password=password)
        return render(request, 'login.html')
    def get(self,request):

        return render(request, 'login.html')



