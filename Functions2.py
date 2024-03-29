# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 09:51:25 2024

@author: Dharesh
"""

# A positional argument is an argument that is passed to a function based on its position in the argument list
# A Keyword argument is passed to a function by specifying the parameter name and its corresponding value

def add(a ,b):
    return a+b
print(add(3, b=4))

def add(c, d):
    return c+d
print(add(6, d=4))

# positional only argumnet passing, slash appending

def add(a, b, /, c):
    return a + b+ c
print(add(3, 4, c=4))
    

# Key word only argumnet

def cylinder_volume(radius, height, *, units='cm^3'):
    return f'{3.14 * (radius ** 2) * height} {units}'

print(cylinder_volume(10, 20))  
#print(cylinder_volume(10, 20, units='mm^3'))
#print(cylinder_volume(10, 20))
#print(cylinder_volume(10, height=20, units='mm^3'))
#print(cylinder_volume(10 ,20))

#The special syntax *args in function definitions in Python is used to pass a
# variable number of arguments to a function. It is used to pass a non-keyworded, 
# variable-length argument list.

def myFun(*args):
    for arg in args:
        print(arg)
#myFun(first='lab', mid='for', last ='python')

#----------ONE EXAMPLE FOR WHOLE LEARNING W.R.T FUNCTIIONS----

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    return year % 4 == 0 and (year % 100 !=0 or year % 400 ==0)


def days_in_month(year, month):
    if not 1<= month <= 12:
        if month == 2 and is_leap(year):
            return 29
        return month_days[month]
    
print (days_in_month(2017,2))

#OUTPUT

#runfile('D:/Python/Lab/Functions2.py', wdir='D:/Python/Lab')
#7
#10
#11
#6280.0 cm^3
#None
