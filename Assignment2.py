# -*- coding: utf-8 -*-


#1.[2,4,1,47,38] sum of the numbers without using built in function

data=[2,4,1,47,38]
sum=0
for i in range(0,5):
    sum=data[i]+sum
print('sum of numbers',sum )    


#2.maximum element in the list

d=[2,4,1,47,38]
maxi=d[0]
for num in d:
    if num>maxi:
        maxi=num
print('Maximum ele',maxi)   

#3.Minimum element in list

d=[2,4,1,47,38]
mini=d[0]
for num in d:
    if(num<mini):
        mini=num
print('minimum ele',mini)        
        
#4.find the avg of the given element in given list

d=[2,4,1,47,38]
sum=0
for i in range(0,len(d)):
    sum +=d[i]
avg=(sum)/len(d)
print('Average',avg)        

#5.search the whether the number is exits or not

d=[2,4,1,47,38]
num=int(input('Enter the number to be searched'))
for i in range(0,len(d)):
    
    
    