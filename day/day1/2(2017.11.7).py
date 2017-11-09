#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haeer

#运算符  **  表示幂数
print(2**8 )
#python默认使用ASCII码进行编译

#打印多行
write='''
第一行
第二行
第三行
第四行
'''
print("多行打印内容：",write)


#简单交互1
name=input("Yourname:")
age=input("Yourage:")
print(type(age))
info='''
-------info of mine-------
Name:%s
Age:%s
'''%(name,age)
print(info)
age_new=int(age)
print(type(age_new))




#简单交互2
name=input("Yourname:")
age=input("Yourage:")
info='''
-------info of mine-------
Name:{_name}
Age:{_age}
'''.format(_name=name,_age=age)
print(info)




#简单交互3
name=input("Yourname:")
age=input("Yourage:")
info3='''
-------info of mine-------
Name:{0}
Age:{1}
'''.format(name,age)
print(info)





















