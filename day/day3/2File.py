#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haeer

book1=open("book3",'r',encoding="UTF-8")
print(book1.tell())
print(book1.readline())
print(book1.tell())  #计数读取的个数
print(book1.read(50))   #读取多少个个数的文本
book1.seek(0)    #回到想要的地方
print(book1.read(50))   #读取多少个个数的文本
print(book1.tell())


print(book1.encoding) #返回文件的编码格式
print(book1.fileno()) #返回一个IO编号
print(book1.seekable()) #返回是否可以使用seek


'''
突发事故有可能没有写进去（停电）
文件可能还在缓存里面
缓存的大小特别小
'''
print(book1.flush())  #强行把放在缓存的文件直接write进去
