# -*- coding: utf-8 -*-

print "Hey %s there." % "you"

my_name = 'Zed A. Shaw'
my = "Zed A. Shaw"
print my_name,my

# %r 就是是非常有用的一个,它的含义是“不管什么都打印出来
# %d 打印数字
# %r 和 %s 有什么不同?
# %r 用来做 debug 比较好,因为它会显示变量的原始数据( raw data ),而其它的符
# 号则是用来向用户显示输出的

x=round(1.7333)
print x

# Hey you there.
# Zed A. Shaw Zed A. Shaw
# 2.0