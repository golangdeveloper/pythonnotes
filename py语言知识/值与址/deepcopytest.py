#  coding:utf-8
import copy


class ClassA:
    def __init__(self,age,name):
        self.A=age
        self.B=name

a=ClassA(10,'我是李鹏')
b=a

c=copy.deepcopy(a)
print id(a),id(b),id(c)