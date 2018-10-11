from django.shortcuts import render
#Create your views here.
from django.views import View
from index.models import *
from django.template import RequestContext
import datetime
class Single(View):
    def get(self,request):
        aid = int(request.GET.get('aid'))
        request.session['aid']=aid
        article = Article.objects.filter(aid=aid)
        comment = Comment.objects.filter(aid=aid)
        return render(request,'single.html',{'comment':comment,'article':article})
    def post(self,request):
        aid=int(request.session.get('aid'))
        pid=Article.objects.get(aid=aid)
        email=request.POST.get('email')
        message=request.POST.get('message')
        Comment.objects.create(aid=pid,email=email,message=message,createtime=datetime.datetime.now())
        article = Article.objects.filter(aid=aid)
        comment = Comment.objects.filter(aid=aid)
        return render(request, 'single.html', {'comment':comment,'article':article})


def form (request):
    return render(request,'form.html')