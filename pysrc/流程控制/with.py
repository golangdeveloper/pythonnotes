# -*- coding: utf-8 -*-
# 自python 2.6开始，成为默认关键字
# Python中的with的作用是自动释放对象，即使对象在使用的过程中有异常抛
# 可以使用with的类型必须实现__enter__ __exit__

def TestWith():
    with open("myfile.txt") as f:
        for line in f:
            print (line)
    f.readline()  # f is already clean up here, here will meet ValueError exception


TestWith()