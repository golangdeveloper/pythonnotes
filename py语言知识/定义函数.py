# -*- coding: utf-8 -*-

# *args 的 * 是什么意思?
# 它的功能是告诉 python 让它把函数的所有参数都接受进来,然后放到名字叫 args 的列表中去。 和你一直在用的 argv 差不多,只不过前者是用在函数上面
# 函数1
def Func1(*args):
    a,b=args
    print a,b

# 函数2
def Func2(a,b):
    print a+b

Func1("lipeng","zhangyue")
Func2("lipeng","zhangyue")