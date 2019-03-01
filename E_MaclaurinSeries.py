# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 19:12:44 2019

@author: Callum
"""
import math
from time import sleep


def eToX(x):
    x = float(x)
    steps = 100
    answer = 0
    i = 0
    n = 2
    
    answer += (1 + x)
    while i < steps:
    
        term = math.pow(x,n)
        term = term / math.factorial(n)
        answer += term
        print(str(i) + ' - ' + str(answer))
        sleep(0.5)
        
        n+=1
        i+=1

    return answer


def sine(x):
    
    x = float(x)
    steps = 100
    answer = 0
    i = 3
    n = 3
    term = 0
    
    answer = x
    
    while i < steps:
        term = 0
        term = math.pow(x,n)
        term = term / math.factorial(n)
    
        
        if i % 2 == 1:
            term = term * -1
            answer += term
        else:
            answer += term

        print(str(i) + ' - ' + str(answer))
        sleep(0.2)
        
        i += 1
        n += 2
    

    
    return answer



def cosine(x):
    
    x = float(x)
    steps = 52
    answer = 0
    i = 1
    n = 2
    answer += 1
    
    while i < steps:
        
        term = math.pow(x,n)
        term = term / math.factorial(n)
        
        if i % 2 == 1:
            term = term * -1
            answer += term
        else:
            answer += term
        
        print(str(i) + ' - ' + str(answer))
        sleep(0.5)
        
        i += 1
        n += 2
        
    return answer