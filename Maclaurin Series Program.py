# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 18:45:04 2019

@author: Callum
"""

"""

Maclaurin Series Program

"""
from E_MaclaurinSeries import eToX, sine, cosine
import math



term = 0

steps = 100

i=0

cmd=''

def control(cmd):
    answer = 0
    cmd = input('  >>>  ')
    if cmd == 'e':
        x = input('Input a value for x ------ ')
        answer = eToX(x)
        print(answer)
        control(cmd)
    elif cmd == 'sine':
        x = input('Input a value for x ------ ')
        answer = sine(x)
        print(answer)
        control(cmd)
    elif cmd == 'cosine':
        x = input('Input a value for x ------ ')
        answer = cosine(x)
        print(answer)
        control(cmd)
    elif cmd == 'end':
        print('See yoo layta')
    else:
        print('Invalid command, try again')
        control(cmd)




#for e^x

    
    

control(cmd)

