# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 10:24:58 2024

@author: Dharesh
"""

my_tuple = (1, 2, 3, 4, 5)
print(len(my_tuple))  # Output: 5


my_tuple = ('a', 'b', 'c', 'a', 'd', 'a')
print(my_tuple.count('a'))  # Output: 3


my_tuple = ('a', 'b', 'c', 'a', 'd', 'a')
print(my_tuple.index('a'))  # Output: 0


my_tuple = (10, 20, 30, 40, 50)
print(max(my_tuple))  # Output: 50



my_tuple = (5, 3, 8, 1, 2)
sorted_tuple = sorted(my_tuple)
print(sorted_tuple)  # Output: [1, 2, 3, 5, 8]


#OUTPUT

#5
#3
#0
#50
#[1, 2, 3, 5, 8]
