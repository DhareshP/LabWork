# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 10:38:47 2024

@author: Dharesh
"""
x = 10
message = "Even" if x % 2 == 0 else "Odd"
print(message)

x = 10
actions = {True: "Even", False: "Odd"}
message = actions[x % 2 == 0]
print(message)


x = 10
get_message = lambda x: "Even" if x % 2 == 0 else "Odd"
print(get_message(x))


x = 10
message = "Even" if x % 2 == 0 and x != 0 else "Odd"
print(message)


x = 10
message = "Even" if x % 2 == 0 and x in {0, 2, 4, 6, 8} else "Odd"
print(message)


#OUTPUT

#Even
#Even
#Even
#Even
#Odd