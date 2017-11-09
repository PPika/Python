#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haeer

string="this is a testing string."
print('**********************************************')
print(string.capitalize())#首字母大写
print(string.count("i"))#统计字符串中的某个字符的个数
print(string.center(50,"-"))#把字符放在中间  字符串的总长度，不足的补充字符
print(string.endswith("ng."))#判断最后是否是ng.
print('**********************************************')
string="this is \ta testing string."
print(string.expandtabs(tabsize=50))#给\t空多少个位数
print('**********************************************')
string="this is a testing string."
print(string.find("is"))#返回的值  切片
print(string[string.find("a"):])
print('**********************************************')
string="{a1} is a testing {a2}."
print(string.format(a1='This',a2='string'))
print(string.format_map({'a1':'This','a2':'string'}))
print('**********************************************')
print('adfa12321321'.isalnum())#判断时候包含数字
print('adfa'.isalpha())#判断时候只有字母
print('12321321'.isdigit())#判断是否是整数
print('3.14'.isdecimal())#判断是否是十进制
print('1A'.isidentifier())#判断是不是一个合法的标识符（变量名）
print('A'.islower())#判断是否小写
print('A'.isupper())#判断是否大写
print('515616165'.isnumeric())#是否只含数字
print(' '.isspace())#是否是空格
print('My name'.istitle())#是否每一个开头的是大写
print(''.isprintable()) # 当tty file 的时候false
print('enheng'.join('++==+'))
print('**********************************************')
print('+'.join((['1','2','3'])))
string="this is a testing string."
print(string.ljust(50,'*'))
print(string.rjust(50,'*'))
print('akafe'.upper())#变大写
print('BUUH'.lower())#变小写
print('\nakfjake\n'.lstrip())#去除左边的换行
print('\nakfjake\n'.lstrip())#去除右边的换行
print('\nakfjake\n'.strip())#去除两边的换行
print('**********************************************')
#加密
ps=str.maketrans('abcdefg','1234567')
print('a good things'.translate(ps))
print('**********************************************')
print('aghaofdsof'.replace('f','F',2))
print('**********************************************')
print('aabbccddeeffgg'.rfind('a'))#从右到左，找到最右边的
print('**********************************************')
print('aa bb cc dd ee ff gg'.split())#将split内的内容当成分割标识
print('1+2\n+3'.splitlines())#功能同上
print('**********************************************')
print('HHIOJIJhioa'.swapcase())#互换大小写
print('HHIOJIJhioa'.title())#开头大写
print('lexaefedeaed'.zfill(50))#不够长度填充








