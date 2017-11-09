#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haeer

#做copy的几种方法

person=['name',['saving',100]]
'''
copy的几种方法（浅）
p1=copy.copy(person)
p2=person[:]
p3=list(person)
'''
p1=person[:]
p2=person[:]
p1[0]='ren1'
p2[0]='ren2'
print(p1,p2)
#用处：有一个共同的账号，有一个人取钱，另一个也会变化
p1[1][1]=50
print(p1,p2)