def Exchange(a,b):
    c=a
    a=b
    b=c
    return a,b

a=1
b=2
c,d=Exchange(a,b)
print a,b,"\n",c,d
