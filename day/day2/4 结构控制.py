#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haeer'


# for i in range(100):
#     print("loop",i)
#
#
# count =0
# while count<100:
#     print("loop",count)
#     count+=1
# else:
#     print("go")
# #需要跳出的时候依旧使用break，使用方法和一般的一样



edibles = ["ham", "spam","eggs","nuts"]
for food in edibles:
    if food == "spam":
        print("No more spam please!")
        break
    print("Great, delicious " + food)
else:
    print("I am so glad: No spam!")
print("Finally, I finished stuffing myself")

