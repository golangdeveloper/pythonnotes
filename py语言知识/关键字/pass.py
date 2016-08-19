
# pass语句什么也不做，一般作为占位符或者创建占位程序，pass语句不会执行任何操作，比如：
while False:
  pass
# pass通常用来创建一个最简单的类：
class MyEmptyClass:
  pass
# pass在软件设计阶段也经常用来作为TODO，提醒实现相应的实现，比如：
def initlog(*args):
  pass #please implement this