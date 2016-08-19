ints=[4,5,3,2,5,6,3,3,5,3,2]
ints.append(5)
ints.insert(3,99)
for i in ints:
    print i,

print "\n",ints.__len__(),ints[3]

for j in range(0,ints.__len__()):
    print ints[j],