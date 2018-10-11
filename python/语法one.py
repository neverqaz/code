#1.缩进结束
#import keyword......print()
'''if a==1:
     func()
print('312312')'''
#2 '' ""  '''  '''字符串
#3注释：1.#   2 ''' '''
#4变量:直接赋值,不限定类型:
#int a;
#String str;
a=1
print(str(type(a)))#打印变量的类型
a="134"
print(str(type(a)))
#数字类型 int long float
a=1
b=2
print(a+b)
c=2**10#2的10次方
print(c)
#布尔类型 True False
#字符串
str1="class%d， class" %a
print(str1)
str2="class{}，class".format(b)#"class{}"相对于字符串也是对象
print (str2)
str3="x{0}, name{1} ,b{0}".format('232','zhangsan')#0，1相对下标
#: 前面是起始下标，后面是结束下标 ，前闭后开
print("str3: "+str3)
print("str3[3:]: "+str3[3:])
print("str3[:3]: "+str3[:3])
print('23gffhgfhf'+str3[3:6])
print("5433536"+str3[::2])#2是步长每2取一次
print("2343242 "+str3[::-1])#倒着输出
 #把str2 d的class 替换成bob
str2=str2.replace("clas",'bob',3)#3是长度
print("新的Str2："+str2)
#字符串查找
print ("index class的下标{}".format(str1.find('class')))
#字符串分割
d2="x y m g"
print(d2.split(' '))
#列表（数组）
print("。。。。。。。。。。。。。。。列表。。。。。。。。。。。。。。。")
mlist=[]
mlist=['shdfg',2435,['232',78],{'name':'zhangsn','age':18}]#字典
print(mlist)
#使用
print(mlist[1])
print(mlist[:3])
print(mlist[:-1])#从0取到倒数第1个
#列表的拼接
mlist1=[1,2,3,'a','b','c']
mlist2=['c','d','e']
#添加
mlist1.append(4)
mlist1.insert(3,'56')
mlist1[2]=33
#查for each
for item in mlist1:
    print(item,end=' ')
print("exit")
#删除
mlist1.pop(2)#根据下标对数据移除
for item in mlist1:
    print(item,end=" ")
print("exit1")
mlist1.remove('c')#根据内容对数据的移除
for item in mlist1:#访问的每一个元素
    print(item,end=" ")
print("exit2")
#列表清空 mlist.clear()
#删除列表 del mlist1
#排序
mlist3=['1','3','45']
mlist3.sort()
print("顺序输出："+str(mlist3))
mlist3.reverse();
print("逆序输出："+str(mlist3))
#列表拼接
mlist3=mlist1+mlist2
print("mlist1+mlist2: "+str(mlist3))
mlist1.extend(mlist2)
print("extend: "+str(mlist1))#/////////////////////////////////////////////////////////////////////////////////////////////////
mlist1.append(mlist2)
print("append:"+str(mlist1))
print("最新mlist1:"+str(mlist1))
print("最新mlist2:"+str(mlist2))

if 'a' in mlist1:#in 和not in 在和不在
    print("yes")
else:
    print("no")

#元组(不可更改只能查)
mtuple=(1,34,56, "sad",'shgsh')
print(mtuple)
print("元组："+str(mtuple))
print(mtuple[3:])
print(len(mtuple))

print(mtuple.index("sad"))
#变量赋值a,b,c=1,2,3
def fun():
	return (1,2,3,4)
#字典 ：单独的字符键值对
mdirct={"name":'zhangsan',"age":20,"height":175}
#字典使用
#查
print(mdirct["name"])
print(mdirct.get("name",0))#如果存在name就拿没有就是默认为0
print(mdirct.keys())
print(mdirct.values())
print(mdirct.items())
#增加
mdirct['sex']='男'
print(mdirct.get("sex",0))
#改

mdirct['name']='lisi'

#删
del mdirct['sex']
print(mdirct)
#del mdirct
#清空 mdirct.clear()
if 'sex' in mdirct:
	print(mdirct['sex'])
else:
	print('不存在')
#运算符
	print(10/3)
	print(10//3)#整除
	print(2**10)
#串行赋值
	a,b,c=1,2,4
	print(a,b,c,end='  ')
	a,b,*c=1,2,3,4,5
	print(a,b,c)
#if a or b or c(a and b//////////not c)
print("hello\n"*10)
#条件
'''if 1:
	pass#空语法体
elif
else:'''
#循环
i=0
while i<10:
	print(i)
	i+=1
for i in['序列',1,344,[123,456,789]]:#[序列化]
            print(i)
        
for item in[[123,456,789],[5678,8900,3456]]:
	for i in item:
		print(i)
for i in list(range(0,10)):
	if i==4:
		continue
	print(i)

#函数
def f(str1,int1):
	print(int1)
	print(str1)
	return int1,str1
#函数调用
print(f('wrer',3))
#作用域(从上之下)
a=0
def f1():
	global a
	print(a)
	a=1
print(a)
print(f1())
#函数传参
def f3(a,b,*args, **kwargs):
	print(a)
	print(b)
	print(args)
	print(kwargs)
def f4(a,b,c=0):
	print(a)
	print(b)
	print(c)	
mtuple=(4,5,6)
mdict={'a':4544,'b':213,'c':643}#该key必须和函数参数一致
f4(mtuple,2)
f4(*mtuple)#传元组进函数一一对应
f4(mtuple,mdict)
f4(**mdict)
f3(1,2,4,654,768,989,m=2323,n=655675)

#类（所有的静态函数没有self（类似this）指针）
class http():
	pass
class fu():
	pass
'''
class Car(http,fu):#继承
	#__c=9
	#color=0
	#name='sk'
	#def_init_(self,c=0,n='mnjhj'):
		#self.color=c
		#self.name=n
	def__del__(self):
		print("被销毁了。。。。")
	def run(self):#self 与类似this一样
		print("{} running".format(self.name))
	def__str__(self):
		print("{} running".format(self.name))'''
#类的使用
'''
c=Car(33,'eyteyt')
print(c.color)
print(c.name)
c.run()
#del c
#导包（模块）
# import 模块名
#from 模块名 import func1
#import numpy as np 。。。。。。。（别名）'''








































