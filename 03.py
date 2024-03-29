# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 09:31:14 2024

@author: tanis
"""
#------------------------------------------------------------------------#
#                              Lists                                     #
#------------------------------------------------------------------------#

#1 ----------------------------------------------------------------------#
#list_1 = ['Biology', 'Maths', 'Physics', 'Science']
#print(list_1)  
#print(len(list_1))
#print(list_1[2])
#print(list_1[-1])

#list_1.append('Computer')
#print(list_1)

#list_1.insert(1, 'Music')
#print(list_1)

#list_2 = ['Hindi','Sanskrit','English']
#list_1.extend(list_2)
#print(list_1)

#print(list_1)  
#list_1.insert(0,list_2)
#print(list_1)  
#print(list_1[2])

#print(list_1)
#list_1.remove('ics')
#print(list_1)
#print(list_1.pop())

#list_1.sort()
#print(list_1)

#print(list_1.index('Science')) # when values exist
#print(list_1.index('pppp')) # error
#print('qqqq' in list_1) #error
#print('Maths' in list_1)

#for item in list_1:
#    print(item)

#for index, item in enumerate(list_1):
#    print(index, item)

#for index, item in enumerate(list_1, start=2):
#    print(index, item)

#list_1 = ['Biology', 'Maths', 'Physics', 'Science']
#list_to_string = ' , '.join(list_1)
#print(list_to_string)
#       OR
#list_to_string = ' - '.join(list_1)
#print(list_to_string)

#new_list = list_to_string.split('-')
#print(new_list)

#Empty Lists
#empty_list = []
#empty_list = list()

#2 ----------------------------------------------------------------------#
#list_3 = ['Tanisha', 'Sakshi', 'Himali', 'Ram']
#print(list_3)  
#print(len(list_3))
#print(list_3[1])
#print(list_3[0])

#list_3.append('Mohan')
#print(list_3)

#list_3.insert(2, 'Geeta')
#print(list_3)

#list_4 = ['Sam','Vihaan','Sonam']
#list_3.extend(list_4)
#print(list_3)
 
#list_3.insert(1,list_4)
#print(list_3)  
#print(list_3[1])

#list_3.remove('shi')
#print(list_3)
#print(list_3.pop())

#list_3.sort()
#print(list_3)

#print(list_3.index('Sakshi')) # when values exist
#print(list_3.index('rrrr')) # error
#print('aaaa' in list_3) #error
#print('Ram' in list_3)

#for item in list_3:
#    print(item)

#for index, item in enumerate(list_3):
#    print(index, item)

#for index, item in enumerate(list_3, start=3):
#    print(index, item)

#list_3 = ['Tanisha', 'Sakshi', 'Himali', 'Ram']
#list_to_string = ' , '.join(list_3)
#print(list_to_string)
#       OR
#list_to_string = ' - '.join(list_3)
#print(list_to_string)

#new_list = list_to_string.split('-')
#print(new_list)

#3 ----------------------------------------------------------------------#
#list_5 = ['Apple', 'Orange', 'Banana', 'Kiwi']
#print(list_5)  
#print(len(list_5))
#print(list_5[3])
#print(list_5[4])

#list_5.append('Grape')
#print(list_5)

#list_5.insert(3, 'Mango')
#print(list_5)

#list_6 = ['Cherry','Guava','Papaya']
#list_5.extend(list_6)
#print(list_5)
  
#list_5.insert(2,list_6)
#print(list_5)  
#print(list_5[3])

#list_5.remove('ana')
#print(list_5)
#print(list_5.pop())

#list_5.sort()
#print(list_5)

#print(list_5.index('Kiwi')) # when values exist
#print(list_5.index('jjjj')) # error
#print('llll' in list_5) #error
#print('Apple' in list_5)

#for item in list_5:
#    print(item)

#for index, item in enumerate(list_5):
#    print(index, item)

#for index, item in enumerate(list_5, start=5):
#    print(index, item)

#list_5 = ['Apple', 'Orange', 'Banana', 'Kiwi']
#list_to_string = ' , '.join(list_5)
#print(list_to_string)
#       OR
#list_to_string = ' - '.join(list_5)
#print(list_to_string)

#new_list = list_to_string.split('-')
#print(new_list)

#4 ----------------------------------------------------------------------#
#num_list1 = [100,10,250,0,-1]
#num_list1.sort()
#print(num_list1)
#num_list1.sort(reverse=True)
#print(num_list1)

#sorted(num_list1)
#print(num_list1)
#new_list1 = sorted(num_list1)
# print(num_list1)
# print(new_list1)

#print(min(num_list1))
#print(max(num_list1))

#5 ----------------------------------------------------------------------#
#num_list2 = [200,500,350,-5,-2]
#num_list2.sort()
#print(num_list2)
#num_list2.sort(reverse=True)
#print(num_list2)

#sorted(num_list2)
#print(num_list2)
#new_list2 = sorted(num_list2)
#print(num_list2)
#print(new_list2)

#print(min(num_list2))
#print(max(num_list2))

#------------------------------------------------------------------------#
#                              Tuples                                    #
#------------------------------------------------------------------------#

#1 ----------------------------------------------------------------------#
#first_tuple = ('a','b','c','d')
#print(first_tuple)

#list_7 = [10,20,30,40,50,60,70,80,90]
#list_8 = list_7  
#print(list_7)
#print(list_8)

#list_7[1] = '100'
#print(list_7)
#print(list_8)

#tuple_1 = ('Biology', 'Maths', 'Physics', 'Science')
#tuple_2 = tuple_1
#print(tuple_1)
#print(tuple_2)

#tuple_1[0] = 'Art'
#print(tuple_1)
#print(tuple_2)

#Empty Tuples
#empty_tuple = ()
#empty_tuple = tuple()

#2 ----------------------------------------------------------------------#
#list_9 = [11,13,15,17,18,19,20,22,24]
#list_10 = list_9  
#print(list_9)
#print(list_10)

#list_9[2] = '30'
#print(list_9)
#print(list_10)

#tuple_3 = ('Tanisha', 'Sakshi', 'Himali', 'Ram')
#tuple_4 = tuple_3
#print(tuple_3)
#print(tuple_4)

#tuple_3[1] = 'Mohan'
#print(tuple_3)
#print(tuple_4)

#3 ----------------------------------------------------------------------#
#list_11 = [1,3,4,5,2,6,7,8,9]
#list_12 = list_11  
#print(list_11)
#print(list_12)

#list_11[3] = '10'
#print(list_11)
#print(list_12)

#tuple_5 = ('Apple', 'Orange', 'Banana', 'Kiwi', 'Grape')
#tuple_6 = tuple_5
#print(tuple_5)
#print(tuple_6)

#tuple_5[2] = 'Mango'
#print(tuple_5)
#print(tuple_6)

#4 ----------------------------------------------------------------------#
#list_13 = [22,24,26,28,30,32,34,36]
#list_14 = list_13  
#print(list_13)
#print(list_14)

#list_13[4] = '40'
#print(list_13)
#print(list_14)

#tuple_7 = ('Lemon', 'Avocado', 'Coconut', 'Jackfruit', 'Pear', 'GreenApple')
#tuple_8 = tuple_7
#print(tuple_7)
#print(tuple_8)

#tuple_7[3] = 'Pomelo'
#print(tuple_7)
#print(tuple_8)

#5 ----------------------------------------------------------------------#
#list_15 = [15,20,21,25,50,55,79,89,70,50]
#list_16 = list_15  
#print(list_15)
#print(list_16)

#list_15[5] = '90'
#print(list_15)
#print(list_16)

#tuple_9 = ('Red', 'Yellow', 'Orange', 'Purple', 'White', 'Brown', 'Black')
#tuple_10 = tuple_9
#print(tuple_9)
#print(tuple_10)

#tuple_9[4] = 'Pink'
#print(tuple_9)
#print(tuple_10)

#------------------------------------------------------------------------#
#                              Sets                                      #
#------------------------------------------------------------------------#

#1 ----------------------------------------------------------------------#
#first_set = {'a','b','c','d','e','f'}
#print(first_set)

# Membership test
#print ('a' in first_set)

#sec_set = {'a','b','c','d','e','f','g','h','i','j','k'}

#print(first_set.union(sec_set))
#print(first_set.intersection(sec_set))
#print(sec_set.difference(first_set))

#Empty Sets
#empty_set = set()

#2 ----------------------------------------------------------------------#
#third_set = {'Tanisha','Sakshi','Siddhi','Ram','Mohan','Rohan'}
#print(third_set)

#print ('Sakshi' in third_set)

#fourth_set = {'Sam','Avi','Sid','Ram','Abhi','Neha'}

#print(third_set.union(fourth_set))
#print(third_set.intersection(fourth_set))
#print(third_set.difference(fourth_set))

#3 ----------------------------------------------------------------------#
#fifth_set = {'Apple', 'Orange', 'Banana', 'Kiwi', 'Grape'}
#print(fifth_set)

#print ('Kiwi' in fifth_set)

#sixth_set = {'Apple', 'Orange', 'Banana', 'Kiwi', 'Grape', 'Mango', 'Cherry'}

#print(fifth_set.union(sixth_set))
#print(fifth_set.intersection(sixth_set))
#print(sixth_set.difference(fifth_set))

#4 ----------------------------------------------------------------------#
#seventh_set = {'Red', 'Yellow', 'Orange', 'Purple', 'White', 'Brown', 'Black'}
#print(seventh_set)

#print ('Red' in seventh_set)

#eighth_set = {'Red', 'Yellow', 'Orange', 'Purple', 'White'}

#print(seventh_set.union(eighth_set))
#print(seventh_set.intersection(eighth_set))
#print(seventh_set.difference(eighth_set))

#5 ----------------------------------------------------------------------#
#ninth_set = {'Jan','Feb','Mar','Apr','May','June','July'}
#print(ninth_set)

#print ('Feb' in first_set)

#tenth_set = {'Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct'}

#print(ninth_set.union(tenth_set))
#print(ninth_set.intersection(tenth_set))
#print(tenth_set.difference(ninth_set))