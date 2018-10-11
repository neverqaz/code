from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic.base import View
import datetime
from .models import *#'.'当前文件
# Create your views here.
def index(request):
   if request.method=="GET":
       return HttpResponse("<h1>GET请求方式请求视图类</h1>"
                           "<form method='post'action='/index/'><input type='submit'/></form>")
   if request.method=="POST":
       return HttpResponse("<h1>post请求方式请求视图类</h1>")
   return render(request,"hello.html")

class F(View):
    def get(self,request):
        print(request.GET)
        a=request.GET.get('a',None)
        b=request.GET.get("b",None)
        print(a,b)
        return HttpResponse("<h1>GET请求方式请求视图类</h1>"
                            "<form method='post' action='/index/'><input type='submit'/></form>"
                            )
    def post(self,request):
        return HttpResponse("<h1>post请求方式请求视图类</h1>")
#通过路径传值
def add(request,a,b):
    return HttpResponse(int(a)+int(b))
def time1(request):
    now=datetime.datetime.now()
    student=[]
    for i in range(0,10):
         data = {}
         data['now']=now
         data['sex']='男'
         data['name']='songyouli'
         data['age']=18
         data['num']=i
         student.append(data)

    #now=[1,2,3,4,5]
   # str="<html><body><h1>it is time:%d</h1></body></html>"% now
   # return HttpResponse(str)
    #return render(request,'time.html',{'now':now})
    #return render(request,'time.html',context=data)
    return render(request, 'time.html', {'student':student})
def  fg(request):
    return render(request,'new.html')
def kg(request):
    return render(request,'search.html')

class FormTest(View):
    def get(self,request):
        return render(request,"form.html")
    def post(self,request):
        request.Session['user_id']=123
        request.Session.get('user_id')
        username=request.POST.get('text',None)
        print("读取到用户名"+username)
        password=request.POST.get('password',None)
        print("读取到密码" + password)
        school=request.POST.get('school',None)
        print("读取到学校" + school)
        car=request.POST.getlist('car',None)#复选框，拿到列表
        print("读取到车" + car)
        print(request.POST)
        return HttpResponse('接受成功')

def sqlTest(request):
    #增
    # Bookinfo.objects.create(book_name='elid'
    #                         ,book_author='hrhr'
    #                         ,book_price=50
    #                         ,book_house='hjddghs'
    #                         ,book_number=34
    #                         ,book_type='fgdfg')
    # return HttpResponse('成功')
   # Bookinfo.objects.create(**request.POST)
   #  book=Bookinfo( book_id=40
   #                 ,book_name='elid'
   #                 ,book_author='hrhr'
   #                 ,book_price=50
   #                 ,book_house='hjddghs'
   #                 ,book_number=34
   #                 ,book_type='fgdfg')
   #  book.save()
    #查
   # print(Bookinfo.objects.all())
    for book in Bookinfo.objects.all():
        print("一本：")
        print(book.book_name,end=' ')
        print(book.book_author,end=' ')
        print(book.book_price, end=' ')
        print(book.book_id, end=' ')
        print(book.book_type, )

    # for book in Bookinfo.objects.filter(book_id=10):#条件查询
    #        print(book.book_name,end=' ')
    for book in Bookinfo.objects.filter(book_id__gt=10,book_author__contains='金',).exclude(book_id=15)[:2]:#条件查询
                      print(book.book_name,end=' ')
    #删
   #
     #改 Bookinfo.objects.filter(book_id=39).delete()
    # book=Bookinfo.objects.get(book_id=10)
    # book.book_name='weqe'
    # book.save()
    # Bookinfo.objects.filter(book_id=10).update(book_name='wwer')
   #  from django.db import connection
   # cursor=connection.cursor()
   # cursor.execute("select * from tables")
    return HttpResponse('seccessg')

class Search(View):
    def list(request):
         type_name1 = Booktype.objects.all()
         hose_name1 = Bookhouse.objects.all()
         return  {'s': type_name1, 'hose': hose_name1}
    # type_name1 = Booktype.objects.all()
    # hose_name1 = Bookhouse.objects.all()
    def get(self,request):
         # return render(request,'search.html',{'s': self.type_name1, 'hose': self.hose_name1})
          return render(request, 'search.html', self.list())
    def post(self,request):

         mdict={}
         mdict['book_name__contains'] = request.POST.get('book_name', '')
         mdict['book_author__contains'] = request.POST.get('book_author', '')
         mdict['book_house__contains'] = request.POST.get('book_house', '')
         mdict['book_type__contains'] = request.POST.get('book_type', '')

         if request.POST.get('book_number')=='':
             pass
         else:
             mdict['book_number'] = int(request.POST.get('book_number',0))
         mdict['book_price__lte'] = int(request.POST.get('maxPrice',1000))
         mdict['book_price__gte'] = int(request.POST.get('minPrice',0))
         print(request.POST.get('minPrice'))
         book=Bookinfo.objects.filter(**mdict)
         return render(request,'list.html',{'books':book})
from django.contrib import auth
def login(request):
    username=request.GET.get('username')
    password = request.GET.get('password')
    user=auth.authenticate(username=username,password=password)
    if user is not None and user.is_active:
        auth.login(request,user)
        return HttpResponseRedirect('/search/')
    else:
        return HttpResponseRedirect('/sql')

def loginout(request):
    auth.logout(request)
    return HttpResponseRedirect('/sql')
