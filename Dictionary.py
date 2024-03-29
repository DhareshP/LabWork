# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 09:55:26 2024

@author: Dharesh
"""

Employee1 = {'name': 'John', 'age': 35, 'Job Profile': 'Data Scientist'}
print(Employee1)
print(Employee1['age'])
print(Employee1.get('shaunk', 'Name does not exist!!!'))
Employee1['Package'] = 60000
Employee1.update({'first': 1, 'second': 2, 'third': 3})
print("Updated:", Employee1)
Employee1.copy() 
print("Copy:", Employee1)
Employee1.clear() 
print(Employee1)
del Employee1['third']
print(Employee1)
Employee1.pop('age')
print(Employee1)
Employee1.popitem()
print(Employee1)
print(len(Employee1))
print(Employee1.keys())
print(Employee1.values())
print(Employee1.items())
for key in Employee1.keys():
    print(key)
for key in Employee1.values():
    print(key)
for key, value in Employee1.items():
    print(key, value)
#-------------------------------------

Employee2 = {'name': 'Emily', 'age': 30, 'Job Profile': 'UX Designer'}
print(Employee2.get('Ema', 'Name does not exist!!!'))
Employee2['Package'] = 70000
Employee2.update({'first': 1, 'second': 2, 'third': 3})
print("Updated:", Employee2)
Employee2.copy() 
print("Copy:", Employee2)
Employee2.clear() 
print(Employee2)
del Employee2['third']
print(Employee2)
Employee2.pop('age')
print(Employee2)
Employee2.popitem()
print(Employee2)
print(len(Employee2))
print(Employee2.keys())
print(Employee2.values())
print(Employee2.items())
for key in Employee2.keys():
    print(key)
for key in Employee2.values():
    print(key)
for key, value in Employee2.items():
    print(key, value)

#-------------------------------------


Employee3 = {'name': 'Michael', 'age': 40, 'Job Profile': 'Project Manager'}
Employee3['Package'] = 75000
Employee3.update({'first': 4, 'second': 5, 'third': 6})
print("Updated:", Employee3)
Employee3.copy() 
print("Copy:", Employee3)
Employee3.clear() 
print(Employee3)
del Employee3['third']
print(Employee3)
Employee3.pop('age')
print(Employee3)
Employee3.popitem()
print(Employee3)
print(len(Employee3))
print(Employee3.keys())
print(Employee3.values())
print(Employee3.items())
for key in Employee3.keys():
    print(key)
for key in Employee3.values():
    print(key)
for key, value in Employee3.items():
    print(key, value)


#-------------------------------------


Employee4 = {'name': 'Alice', 'age': 27, 'Job Profile': 'Software Engineer'}
Employee4.copy() 
print("Copy:", Employee4)
Employee4.copy() 
print("Copy:", Employee4)
Employee4.clear() 
print(Employee4)
del Employee4['third']
print(Employee4)
Employee4.pop('age')
print(Employee4)
Employee4.popitem()
print(Employee4)
print(len(Employee4))
print(Employee4.keys())
print(Employee4.values())
print(Employee4.items())
for key in Employee4.keys():
    print(key)
for key in Employee4.values():
    print(key)
for key, value in Employee4.items():
    print(key, value)


#-------------------------------------


Employee5 = {'name': 'Sophia', 'age': 33, 'Job Profile': 'Marketing Specialist'}
Employee5.clear() 
print(Employee5)
Employee5.copy() 
print("Copy:", Employee5)
Employee5.clear() 
print(Employee5)
del Employee5['third']
print(Employee5)
Employee5.pop('age')
print(Employee5)
Employee5.popitem()
print(Employee5)
print(len(Employee5))
print(Employee5.keys())
print(Employee5.values())
print(Employee5.items())
for key in Employee5.keys():
    print(key)
for key in Employee5.values():
    print(key)
for key, value in Employee5.items():
    print(key, value)

#OUTPUT

#runfile('D:/Python/Lab/Dictionary.py', wdir='D:/Python/Lab')
#{'name': 'John', 'age': 35, 'Job Profile': 'Data Scientist'}
#35
#Name does not exist!!!
#Updated: {'name': 'John', 'age': 35, 'Job Profile': 'Data Scientist', 'Package': 60000, 'first': 1, 'second': 2, 'third': 3}
#Copy: {'name': 'John', 'age': 35, 'Job Profile': 'Data Scientist', 'Package': 60000, 'first': 1, 'second': 2, 'third': 3}