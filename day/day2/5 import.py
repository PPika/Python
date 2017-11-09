#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haeer



'''模块的导入是直接讲.py文件导入就行，注意文件存放的位置即可'''


#导入模块
import sys
print(sys.path)#打印环境变量
print(sys.argv)#打印了脚本的绝对路径（Pycharm的原因）
#在控制台的打印结果不一样
# print(sys.argv[2])   只有在控制台可以使用

import os
#系统交互模块
# cmd_result=os.system("dir")
# os.mkdir("new dir")   创建一个新的目录
cmd_read=os.popen("dir").read() #讲结果存在一个临时地址
print(cmd_read)
