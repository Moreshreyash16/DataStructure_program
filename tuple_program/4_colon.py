'''
@Author: Shreyash More

@Date: 2023-06-9 23:10:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-09 23:10:30

@Title :  Write a Python program to create the colon of a tuple.


'''
import copy
 
user_tuple = (1, 2, (3, 5), 4)
 
# using copy for shallow copy
li2 = copy.copy(user_tuple)
print("li2 ID: ", id(li2), "Value: ", li2)
# using deepcopy for deepcopy
li3 = copy.deepcopy(user_tuple)
print("li3 ID: ", id(li3), "Value: ", li3)