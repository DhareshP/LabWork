# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 09:39:48 2024

@author: Dharesh
"""

#Numpy is a python library written in c and, it's N-dimensional array

import numpy as np
#1D

arr = np.arange (5)
print(arr)
print(type(arr))
#antother way, as argument
arr = np.array([1,2,3])
print(arr)
print(type(arr))


#attributes of the array

print(arr.dtype)
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.itemsize)#bytes reqd to store on data item

arr_one = np.array([1.0,2,3])
print(arr_one.dtype)
print(arr_one)

array = np.array([[1,2,3],
                  [4,5,6]])
print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.itemsize)

#3D

arr = np.array([[
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ],
    [
     [1,2,3],
      [4,5,6],
      [7,8,9]
      ]
    ])

print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.size)

#Special Arrays

arr = np.ones((2,3,4))
print(arr)

arr = np.random.randn(2,3)
print(arr)

#indexing

arr = np.array([
    [[1,2,3],
     [4,5,6],
     [7,8,9]
     ],
    [[10,20,30],
     [40,50,60],
     [70,80,90]
     ]
    ])

print(arr[0,0,0])
print(arr[1,0,2])
print (arr [:,:,:])
print (arr [0,:,:])
# print ( arr [1,:,:])
# print ( arr [:,1,:])
# print (arr [:,0:1,:])
