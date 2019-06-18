# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 15:06:26 2019

@author: Manasa
"""

def sum(num1,num2):
    result=num1+num2
    print('result',result)  #definig
    
sum(100,39)     #calling

def sum(num1,num2):
    result=num1+num2
    return result  #definig
    
res=sum(141,39)     #calling    
print('res',res)