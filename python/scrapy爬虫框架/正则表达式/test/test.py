import re
line='bobby123'
# if line=='bobby123':
#     pass
#定义模式regex_str14

regex_str="^b.*3$"
#'^b'代表b开始字符， ‘.’代表任意字符，‘*’代表 前面的字符可以重复恒多变,'3$'必须以‘3’结尾

#'+'代表加号前面的字符至少出现一次

line1='booooooobby123'
regex_str3=".*?(b.+?b).*"
#提取booooooob ’？‘打破贪婪匹配
regex_str2=".*?(b.*?b).*"#'?'表示从左边的第一个符合?(b, ?b
result=re.match(regex_str2,line1)
if result:#(模式字符串，匹配字符串)
    print(result.group(1))#提取模式括号里的内容
    print('yes')
else :
    print('no')
regex_str1="^b.3$"#模式定义是匹配三个字符
if re.match(regex_str1,line):#(模式字符串，匹配字符串)
    print('yes')
else :
    print('no')
#{2} {2,} {2,5}代表出现前面字符的次数分别2次，2次以上，2以上5以下
regex_str6=".*(b.{2,5}b).*"
#’|‘或的关系
line5='bobby123'
regex_str7="bobby|bobby123"#该模式是bobby或者是Bobby123都可以
regex_str8="((boobby|bobby)123)"
req=re.match(regex_str8,line5)
if req :
    print('req.group(1):'+req.group(1))
    print("req.group(2):"+req.group(2))
#'[]'代表中括号里的任意字符都可以匹配
line7='xobby123'
regex_str9="([azsx]obby123)"#该模式是字符第一位只要出现a，z，s，x都可以匹配

req1=re.match(regex_str9,line7)
if req1 :
    print('req1.group(1):'+req1.group(1))
line8='18548019624'
regex_str10="(1[48357][0-9]{8}[^1]$)"#该模式[0-9]0-9中的任意字符出现9次并且最后一位不等于1
#'[*.mkjj]'代表× .没有被转yi
req2=re.match(regex_str10,line8)
if req2 :
    print('req2.group(1):'+req2.group(1))
#\s 代表空格的意思
#\S代表不为空格的意思
#\w代表任意字符包括【A-Za-z0-9_】
#\W代表不为任意字符
line9='你 好'
regex_str11="(你\s好)"#该模式你好中间出现空格字符匹配
regex_str12="(你\S+好)"#该模式你好中间不出现空格字符匹配
#'[*.mkjj]'代表× .没有被转yi
req3=re.match(regex_str11,line9)
if req3 :
    print('req3.group(1):'+req3.group(1))
#[\u4E00-\u9FA5]代表提取出现连续汉字
line11='study in 北京大学'
regex_str14=".*?([\u4E00-\u9FA5]+大学)"
req4=re.match(regex_str14,line11)
if req4:
    print(req4.group(1))
#'\d'代表数字
line16='QQ出生于2001年'
regex_str14='.*?(\d+)年'#或者是'.*(\d{4})年'
req5=re.match(regex_str14,line16)
if req5:
    print(req5.group(1))
#例子
line123='xxx出生于2001年6月1日'
line123='xxx出生于2001/6/1'
line123='xxx出生于2001-6-1'
line123='xxx出生于2001-06-01'
line123='xxx出生于2001-06'
regex_str142='.*出生于(\d{4}[年/-]\d{1,2}([月/-]\d{1,2}|[月/-]$|$))'