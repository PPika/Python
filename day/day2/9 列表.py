#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haeer
import copy

name=["张三","张五","李七"]
name2=name.copy()
print(name,name2)
print("*********************************************************")
name3=["张三",["张三","张五","李七"],"张五","李七"]
name4=name3.copy()
print(name3)
print(name4)
print("*********************************************************")
name3[0]="zhangsan"
name3[1][0]="zhangsan"
print(name3)
print(name4)
#它拷贝的是内存地址，所以列表内的列表没有改变
#这种方法叫做浅copy  第二个对第一个的引用
print("*********************************************************")
#依赖导入的copy
name4=copy.deepcopy(name3)
print(name4)  #完整的复制
print("*********************************************************")
#切片中0和-1可以省略
number=["1","2","3","4","5"]
for i in number:
    print(i)
print("*********************************************************")
print(number[::2])
print(number[::1])
print(number[::3])
print("*********************************************************")
print(number[0:-1:2])
print(number[0:-1:1])
print(number[0:-1:3])
print("*********************************************************")