# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 23:31:06 2024

@author: Dharesh
"""
#mutable 
def mutable_example(*args, **kwargs):
    args_list = list(args) 
    kwargs_copy = dict(kwargs)  

    args_list.append(4) 
    kwargs_copy["key3"] = "python lab" 

    print("Modified args:", args_list)
    print("Modified kwargs:", kwargs_copy)

mutable_example(2, 4, 6, key1='Hello', key2='python')


#Immutable

def Immutable_example(*args, **kwargs):
    args_tuple = tuple(args)
    kwargs = dict(kwargs)
    args_tuple = tuple(args)
    args_tuple[0] = 100
    
    kwargs["new_key"] = "New keyname"
    
    print("Unmodified args:", args_tuple)
    print("Modified kwargs:", kwargs)
Immutable_example(2, 4, 6, key1='Hello', key2='python')
