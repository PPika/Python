#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haeer
'''
book=open("book.txt",encoding="UTF-8").read()
文本的读取  #必须限定文件的编码格式
'''


#
#这里是通过读的方式来写   相当于重写创建了一个文件
#
# book=open("book.txt",'w',encoding="UTF-8")
# f=book.read()
# print(f)
# #print("00",f)   这里有一个错误是因为Windows系统的问题
# book.write("xie")



'''
规范的写法
book=open("book.txt",'w(r)',encoding="UTF-8")
'''


book2=open("book2",'w',encoding="UTF-8")
book2.write("jjjjjjjjjjjjjjjjjjjjjjjjjj\n")
book2.write("jjjjjjjjjjjjjjjjjjjjjjjjjj\n")
book2.close()


book2=open("book2",'a',encoding="UTF-8")
#a  append  添加
book2.write("aaaaaaaaaaaaaaaaaaaaaaaaaj\n")
book2.write("aaaaaaaaaaaaaaaaaaaaaaaaaa\n")
book2.close()





















