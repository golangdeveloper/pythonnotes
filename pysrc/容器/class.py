# -*- coding: utf-8 -*-

import mystuff_module

mystuff={'apples':[1,2,3]}
# dict style
mystuff['apples']
# module style
mystuff_module.apples()

print mystuff_module.tangerine
# class style
class MyStuff:
    def apple(self):
        print ""

    def __init__(self):
        self.tangerine = "And now a thousand years between"

thing = MyStuff()
thing.apple()
print thing.tangerine