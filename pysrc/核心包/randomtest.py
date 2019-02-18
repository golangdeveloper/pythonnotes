import random

WORDS=['wfwf','32vd23','ndfgs','h67jrc']
snippet='sdfw###23###havwe###'

r=random.sample(WORDS, snippet.count("###"))
print r
