# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 14:06:36 2019

@author: Manasa
"""

name=input('Enter name ')
print(type(name))
print('your name is',name)

age=int(input('Enter age'))
print(type(age))
print('your age is',age)

amount=float(input('Enter amount'))
print(type(amount))
print('you have to pay',amount)

#opeartors
# + , - , * , / , % , =,+=,*=,//

num1=int(input('Enter number 1'))
num2=int(input('Enter number 2'))
result=num1+num2
print('result of addition of',num1,',',num2,' is',result)

print(10/3)
print(10//3) #display only integer part

sum=0
sum=sum+10
sum +=10
print(sum)

#Relational
# >,<,>=,<=,!=

num1=100
num2=200
print(num1>num2)
print(num1<num2)
print(num1!=num2)

# ==,===
num3=100
print(num1==num3)

#logical operators
# and , or ,not
print(num1>num2 and num1>num3)



