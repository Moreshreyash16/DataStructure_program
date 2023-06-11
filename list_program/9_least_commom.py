'''
@Author: Shreyash More

@Date: 2023-06-09 14:32:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-09 14:32:30

@Title :    Write a Python function that takes two lists and returns True if they have at
least one common member.

'''

def one_common(arr,arr2):
    """
    Description:
        It find if they have at least one common member.
    Parameter:
        Takes two array as input 
    Return:
       Returns a boolean value
    """
    
    for i in arr:
        if i in arr2:
            return True
        else:
            return False

def main():
    arrays=list(map(int,input("Enter numbers: ").split()))
    arrays_2=list(map(int,input("Enter numbers: ").split()))
    print(one_common(arrays,arrays_2))
    

if __name__=="__main__":
    main()