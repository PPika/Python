#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haeer

'''
对象：
对象是一个实体
现实中实体和实体之间的交互解决现实问题：人和车，人开车达到跑
'''
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_Person(self,):
        return "<Person (%s,%s)>"%(self.name,self.age)
p = Person("Josn",32)
print(type(p))
print(id(p))
print(p)
print(p.age)
print(p.name)