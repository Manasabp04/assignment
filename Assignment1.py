# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 15:21:40 2019

@author: Manasa
"""

#2.write a function to find simple interest

def si():    
    P=float(input('Enter the per:'))
    T=float(input('Enter the time:'))
    R=int(input('Enter the rate:'))
    si=(P*T*R)/100
    print('simple interest is',si)

si() 


#1.print 12's tables in reverse order

for i in range(10,0,-1):
    res=12*i
    print('12 * ',i,'=',res)
    
#3.print prime numbers btw two numbers.

num1=int(input('Enter num1:'))
num2=int(input('Enter num2:'))

print('The prime number btw',num1,'and',num2,'are')

for num in range(num1,num2):
    
    if(num > 1):
        for i in range(2,num):
            if(num % i) == 0:
                break
        else:
                print(num)

#4.fibonoacci series

num=int(input('Enter the range:'))
i = 0
First_Value = 0
Second_Value = 1
           
# Find & Displaying Fibonacci series
while(i < num):
           if(i <= 1):
                      Next = i
           else:
                      Next = First_Value + Second_Value
                      First_Value = Second_Value
                      Second_Value = Next
           print(Next)
           i = i + 1  

#5.find the bill to be paid

meter=int(input('Enter the unit consumed:'))
if(meter<=100):
    bill=meter*2
elif(100<meter and meter<=200):
    bill=meter*3
elif(200<meter and meter<=300):
    bill=meter*5
else:
    bill=meter*6
print('your bill is rupee',bill)              
