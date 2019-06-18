# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 19:44:58 2019

@author: Manasa
"""

str='helloworld'
value=str[::-1]
print(value)

print("xyyzxyzxzxyy".count('yy'))


def say(message, times = 1):
    print(message * times)
say('Hello')
say('World', 5)

y, z = 1, 2
def f():
    global x
    x = y+z
    
def m(list):
    v = list[0]
    for e in list:
      if v < e: v = e
    return v
 
values = [[3, 4, 5, 1], [33, 6, 1, 2]]
 
for row in values: 
    print(m(row), end = " ")
    
