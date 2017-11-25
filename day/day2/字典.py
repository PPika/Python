#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haeer

#Key——Value数据类型 （键值对）
info={
    'k1':'aa',
    'k2':'bb',
    'k3':'cc',
}

print(info)
#字典是无序的
print(info['k2'])
#通过Key的到Value
info['k4']='dd'
print(info)
#删除方法一
del info['k4']
print(info)
#删除方法二
info.pop('k1')
print(info)
#info.popitem   随机删除
#安全的获取Key值
print(info.get('k5'))
print('k2' in info)


###################多级字典嵌套########################
info_a ={
    'key':{
        'k1':['a1','a2','a3'],
        'k2':['b1','b2','b3'],
    }
}
info_a['key']['k1'][1]='ddddddddddddddddddddddddddddd'
print(info_a)
###################其他函数########################
