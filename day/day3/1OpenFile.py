#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haeer

'''
book=open("book1",encoding="UTF-8").read()
文本的读取  #必须限定文件的编码格式
'''


#
#这里是通过读的方式来写   相当于重写创建了一个文件
#
# book=open("book1",'w',encoding="UTF-8")
# f=book.read()
# print(f)
# #print("00",f)   这里有一个错误是因为Windows系统的问题
# book.write("xie")



'''
规范的写法
book=open("book1",'w(r)',encoding="UTF-8")
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

book3=open("book2",'r',encoding="UTF-8")
for i in range(3):
    print(book3.readline())

book4=open("book2",'r',encoding="UTF-8")
for line in book4.readlines():
    print(line.strip())


'''
大型的文件
readlines特别占用内存
方法：循环一个raadline()，删除一个
'''
#一个huge的循环方法
book5=open("book3",'r',encoding="UTF-8")
count=0
for line in book5:
    if count ==2:
        print("____________________分割线______________________")
        count+=1
        continue
    print(line)
    count+=1














