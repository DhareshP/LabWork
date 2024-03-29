# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 10:04:32 2024

@author: Dharesh
"""

list_1 = ['apple', 'banana', 'orange', 'grape']
print(list_1)

print(list_1)  
print(len(list_1))
print(list_1[2])
print(list_1[-1])

list_1.append('Mango')
print(list_1)

list_1.insert(1, 'Peach')
print(list_1)

list_2 = [1, 2, 3, 4]
print(list_2)


print(list_1)  
list_1.insert(0,list_2)
print(list_1)  
print(list_1[2])

print(list_1)
list_1.remove('grape')
print(list_1)
print(list_1.pop())

list_1.sort()
print(list_1)

print(list_1.index('orange')) # when values exist
print(list_1.index('pppp')) # error
print('qqqq' in list_1) #error
print('orange' in list_1)

for item in list_1:
    print(item)

for index, item in enumerate(list_1):
    print(index, item)
#or index, item in enumerate(list_1, start=2):
#    print(index, item)

list_1 = ['apple', 'banana', 'orange', 'grape']
list_to_string = ' , '.join(list_1)
print(list_to_string)
#------OR
#list_to_string = ' - '.join(list_1)
#print(list_to_string)

#new_list = list_to_string.split('-')
#print(new_list)

#Empty Lists
#empty_list = []
#empty_list = list()

#2 ----------------------------------------------------------------------#
list_3 = ['dog', 'cat', 'bird', 'fish']
print(list_3)
 
print(len(list_3))
print(list_3[1])
print(list_3[0])

list_3.append('Mammals')
print(list_3)

list_3.insert(2, 'Crocodile')
print(list_3)

list_4 = ['Monday', 'Tuesday', 'Wednesday', 'Thursday']
list_3.extend(list_4)
print(list_3)
 
list_3.insert(1,list_4)
print(list_3)  
print(list_3[1])

list_3.remove('Mon')
print(list_3)
print(list_3.pop())

list_3.sort()
print(list_3)

print(list_3.index('Thursday')) # when values exist
print(list_3.index('rrrr')) # error
print('aaaa' in list_3) #error
print('Thursday' in list_3)

for item in list_3:
    print(item)

for index, item in enumerate(list_3):
    print(index, item)

for index, item in enumerate(list_3, start=3):
    print(index, item)

list_3 = ['Tanisha', 'Sakshi', 'Himali', 'Ram']
list_to_string = ' , '.join(list_3)
print(list_to_string)
#       OR
#list_to_string = ' - '.join(list_3)
#print(list_to_string)

#new_list = list_to_string.split('-')
#print(new_list)

#3 ----------------------------------------------------------------------#
list_5 = [10.5, 20.3, 15.7, 8.2]
print(list_5)

 
print(len(list_5))
print(list_5[3])
print(list_5[4])

list_5.append('9.9')
print(list_5)

list_5.insert(3, '6')
print(list_5)

list_6 = ['Cherry','Guava','Papaya']
list_5.extend(list_6)
print(list_5)
  
list_5.insert(2,list_6)
print(list_5)  
print(list_5[3])

list_5.remove('ana')
print(list_5)
print(list_5.pop())

list_5.sort()
print(list_5)

print(list_5.index('Peach')) # when values exist
print(list_5.index('jjjj')) # error
print('llll' in list_5) #error
print('Apple' in list_5)

for item in list_5:
    print(item)

for index, item in enumerate(list_5):
    print(index, item)

for index, item in enumerate(list_5, start=5):
    print(index, item)

list_5 = ['Apple', 'Orange', 'Banana', 'Kiwi']
list_to_string = ' , '.join(list_5)
print(list_to_string)
#       OR
#list_to_string = ' - '.join(list_5)
#print(list_to_string)

#new_list = list_to_string.split('-')
#print(new_list)

#4 ----------------------------------------------------------------------#
num_list1 = [100,10,250,0,-1]
num_list1.sort()
print(num_list1)
num_list1.sort(reverse=True)
print(num_list1)

sorted(num_list1)
print(num_list1)
new_list1 = sorted(num_list1)
print(num_list1)
print(new_list1)

print(min(num_list1))
print(max(num_list1))

#5 ----------------------------------------------------------------------#
num_list2 = [4000,4500,9350,-10,-2]
num_list2.sort()
print(num_list2)
num_list2.sort(reverse=True)
print(num_list2)

sorted(num_list2)
print(num_list2)
new_list2 = sorted(num_list2)
print(num_list2)
print(new_list2)
print(min(num_list2))
print(max(num_list2))


#OUTPUT

runfile('D:/Python/Lab/lists.py', wdir='D:/Python/Lab')
['apple', 'banana', 'orange', 'grape']
['apple', 'banana', 'orange', 'grape']
4
orange
grape
['apple', 'banana', 'orange', 'grape', 'Mango']
['apple', 'Peach', 'banana', 'orange', 'grape', 'Mango']
[1, 2, 3, 4]
['apple', 'Peach', 'banana', 'orange', 'grape', 'Mango']
[[1, 2, 3, 4], 'apple', 'Peach', 'banana', 'orange', 'grape', 'Mango']
Peach
[[1, 2, 3, 4], 'apple', 'Peach', 'banana', 'orange', 'grape', 'Mango']
[[1, 2, 3, 4], 'apple', 'Peach', 'banana', 'orange', 'Mango']
Mango