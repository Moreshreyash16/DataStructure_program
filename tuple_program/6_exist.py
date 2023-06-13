'''
@Author: Shreyash More

@Date: 2023-06-9 23:10:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-09 23:10:30

@Title :  Write a Python program to check whether an element exists within a tuple.


'''

def exist(tuples,value):
    """
    Description:
        It gives duplicate element from tuple
    Parameter:
        tuples:Takes array as an tuple
        value:Takes value as an tuple
    Return:
       Returns a repeated element
    """
    if value in tuples:
        return True
    else:
        return False

def main():
    user_tuple=tuple(input("Enter numbers: ").split())
    value=input("enter a value to find")
    print(f" {exist(user_tuple,value)} ")
    

if __name__=="__main__":
    main()