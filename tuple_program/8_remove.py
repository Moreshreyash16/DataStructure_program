'''
@Author: Shreyash More

@Date: 2023-06-9 23:10:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-09 23:10:30

@Title :  Write a Python program to remove an item from a tuple.


'''

def remove_element(input_tuples,value):
    """
    Description:
        It removes the given element
    Parameter:
        input_tuples:Takes array as an tuple
        value:takes value as input
    Return:
       Returns a repeated element
    """
    input_tuples=list(input_tuples)
    input_tuples.remove(value)
    input_tuples=tuple(input_tuples)
    return input_tuples

def main():
    user_tuple=tuple(input("Enter numbers: ").split())
    print(f" The original array is {user_tuple} ")
    value=int(input("enter a value to remove: "))
    print(f" {remove_element(user_tuple,value)} ")
    

if __name__=="__main__":
    main()