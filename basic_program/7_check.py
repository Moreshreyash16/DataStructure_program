'''
@Author: Shreyash More

@Date: 2023-06-07 15:35:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-07 15:35:30

@Title :Write a Python program to check whether a specified value is contained in a group of values.
'''
def check(arr,value):
    """
    Description:
        It checks if value is array
    Parameter:
        Takes array and value as a input 
    Return:
       Returns true if value is present
    """
    if value in arr:
        return True
    else:
        return False

def main():
    array=[4,8,6,5]
    value=5
    print(check(array,value))


if __name__=="__main__":
    main()