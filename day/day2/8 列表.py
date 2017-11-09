#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haeer

name=["张三","张五","李七"]
for i in range(3):
    print(i,name[i])
print("*****************************")
print(name[0:3])#切片
print(name[-2])
print(name[-3:-1])
print(name[-3:0])
print(name[-3:1])
print(name[-3:2])
print(name[-3:])
print(name[-2:])
print(name[:2])
print("*****************************")
name.append("插入1")
for i in range(4):
    print(i,name[i])
name.insert(1,"插入3")
for i in range(5):
    print(i,name[i])

name[0]="修改了你"
print(name[0])
print("*****************************")
name.remove("插入1")
for i in range(4):
    print(i,name[i])
print("*****************************")
name.pop()
#不输入参数默认删除最后一个
for i in range(3):
    print(i,name[i])
print("*****************************")
# 找到元素的位置
print(name.index("修改了你"))
print(name[name.index("修改了你")])
print("*****************************")
#元素的个数
print(name.count("删除1"))
print("*****************************")
name.reverse()#反转
name.sort()#排序     按照ASCII码排序的方式
# name.clear()         清空所有的元素
print("*****************************")
name2=[1,2,3,4]
name.extend(name2)
print(name2)
print("*****************************")
del name2
print(name)
#这个时候的name2已经消失   再进行打印就会失败