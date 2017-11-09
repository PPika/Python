#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haeer

#编码和解码
a="操作不对啊"
print(a.encode(encoding="utf-8"))
# 编码
#输出结果的最前的b表示是二进制的编码
print(a.encode(encoding="utf-8").decode())
#解码