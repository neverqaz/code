# import hello
# from hello import func1
# from hello import *
# import numpy as np

# 变量
'''
a = 1
print(str(type(a)))
a = "123"
print(str(type(a)))
'''
# 数字类型
a = 1
b = 1.5
print("整型和浮点型相加：{}".format(a+b))
c = 2**100
print("2的100次方：%d " % c)

# 字符串
str1 = "class%d" % a
print("通过%拼接的字符串："+str1)
str2 = "class{}".format(a)
print("通过{}拼接的字符串："+str2)
str2 = "hello {0} , your height is {1}, {0} bye!".format('bob',175)
print(str2)
# : 前面是起始下标，后面结束下标，前开后闭
print("3 index of str2: "+str2[5:1:-2])
# 把bob  全部替换成Tom(注意返回新的字符串)
print('index of bob is : {}'.format(str2.find('bob')))
str2 = str2.replace('bob','Tom')
print(str2)
print(str2.split(' '))

# 列表
mlist = [] # 声明空列表
mlist = ['sdfgh',6543,['asd',54],{'name':'zhangsan','age':18}]
print(mlist)
print(mlist[1])
print(mlist[:3])
print(mlist[:-2]) # 表示从0，取到倒数第三个（前闭后开）
mlist1 = [1,2,3,'a','b','c']
mlist2 = ['d','e','f']
# # 增
mlist1.append(4)
mlist1.insert(3,5)
print(mlist1)
# # 改
mlist1[2] = 33
print(mlist1)
# # 查
for item in mlist1:
    print(item)
print('结束循环')
# 删除
mlist1.pop(2)
print(mlist1)
mlist1.remove('a')
print(mlist1)
# del mlist1 # 删除了变量
mlist1.clear() # 清空
print(mlist1)
# 排序
mlist1 = [1,2,38,6,4,6,6,34,65,3,65,76,3464,45]
print('before sort:' + str(mlist1))
mlist1.sort()
print('after sort:'+ str(mlist1))
# 列表的拼接
print(mlist1 + mlist2)
mlist1.extend(mlist2)
print(mlist1)
# in 和 not in
if 'asf' not in mlist1:
    print('yes')
else:
    print('no')
# 元祖
mtuple = (1,33,5,7,"234",'asd')
print(mtuple[3])
print(mtuple[:3])
print(len(mtuple))
print(mtuple.index('234'))
# 字典
mdict = {"name":'张三',"age":20,"height":175}
# 查
print(mdict['name']) # 张三
print(mdict.get('sex','男'))
print(mdict.items())
print(mdict.keys())
print(mdict.values())
# 增
mdict['sex'] = '男'
print(mdict)
# 改
mdict['name'] = '李四'
print(mdict)
# 删
del mdict['sex']
print(mdict)
mdict.clear()
print(mdict)
# del mdict # 删掉了整个字典
if 'sex' in mdict: # 判断是否存在某一个键
    print(mdict['sex'])
else:
    print(' 不存在 ')
# 运算符和表达式
print(10/3)
print(10//3)
# 串行赋值
a,b,c = 1,2,3
print(a,b,c,end='   ')
a,b,*c = 1,2,3,464,5,"q34","43rtft"
print(a,b,c)
print("输入一百个hello briup：")
print("hello briup!  " * 100)

#从1输出到100
'''
i = 0;
while i <= 100:
    print(i)
    i += 1
for i in range(0,100):
    if i == 50 :
        continue
    print(i)
'''
for item in [[123,123,123],[321,321,321]]:
    for i in item:
        print(i)

a = 0
def func():
    global a
    print(a)
    a = 1
print(a)

def func2(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

mtuple = (4,5,6)
mdict = {'a':7,'b':8,'c':9}

func2(**mdict)

func()

# 面向对象

def get_class_name():
    pass
class Car(object):

    def __init__(self,c=0,n='SKODA'):
        self.color = c
        self.name = n
    def __del__(self):
        print('被销毁...')
    def __str__(self):
        return self.name

    def run(self):
        print("{} running".format(self.name))

c = Car(1,"BMW")
print(c.color)
print(c.name)
print(c)
c.run()
c = Car()











#
