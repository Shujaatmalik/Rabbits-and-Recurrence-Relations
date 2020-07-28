# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 14:09:08 2020

@author: Shujaat
"""

    
def febonacci_loop(number,OffSpring):
    old=1
    new=1
    for i in range(number-1):
        tem=new
        new=old
        old=old+tem*OffSpring

    return new
print(febonacci_loop(30,5))
