# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 14:53:03 2019

@author: Manasa
"""
#create a car class having a constructor

class car():
    def __init__(self,make,model,color,price):
        self.make=make
        self.model=model
        self.color=color
        self.price=price
        self.speed = 0
        
    def start(self):
        self.speed = 0
        return self.speed 
        
    def move(self):
        self.speed = self.speed + 5
        return self.speed
            
    def stop(self):
        self.speed = 0
        return self.speed 
        
    def info(self):
        print('The car is made in the',self.make)
        print('The model of the car is',self.model)
        print('The color of the car is',self.color)
        print('The price of the car is',self.price)
        #print('The speed of the car is',self.speed)

Dzire=car('Maruthi','zei','purlwhite',60000000)
Dzire.info()
initial_speed=Dzire.start()
print('The initial speed is',initial_speed)
Dzire.start()
speed=Dzire.move()
Dzire.move()
print('The speed of the car',speed)  
Dzire.stop()




