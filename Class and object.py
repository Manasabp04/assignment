# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 09:46:21 2019

@author: Manasa
"""

class student():
    def register(self,regno,name,standard,section):
        self.regno=regno
        self.name=name
        self.standard=standard
        self.section=section
        
    def information(self):
        print('Regno',self.regno,'name',self.name,'standard',self.standard,'section',self.section)
 
Mounika=student()
Mounika.register('85','Mounika','3','B')
Mounika.information()

Rashi=student()
Rashi.register('123','Rashi','4','B')
Rashi.information()
       
        
        