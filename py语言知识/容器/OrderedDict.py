import collections

d = {'banana':3,'apple':4,'pear':1,'orange':2}

orderedd=collections.OrderedDict(
    sorted(d.items(),key = lambda t:t[0])
)

print orderedd