# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 09:57:14 2019

@author: Manasa
"""

class calcu():
    def add(self,num1,num2):
        return num1+num2
    
    def sub(self,num1,num2):
        return num1-num2
        
    def mul(self,num1,num2):
        return num1*num2
        
    def div(self,num1,num2):
        return num1/num2

calculator=calcu()
result=calculator.add(35,34)
print('Result of addition is',result)

cal2=calcu()
result=cal2.sub(35,34)
print('Result of substraction is',result)

cal3=calcu()
result=cal3.mul(35,34)
print('Result of multiplication is',result)

cal4=calcu()
result=cal4.div(35,34)
print('Result of division is',result)
