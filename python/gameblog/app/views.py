from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
import datetime
# Create your views here.

# url(r'^about/$', views.about),
#     url(r'^contact/$', views.contact),
#     url(r'^gallery/$', views.gallery),
#     url(r'^singlepost/$', views.singlepost),

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def gallery(request):
    return render(request,'gallery.html')

def singlepost(request):
    return render(request,'single-post.html')