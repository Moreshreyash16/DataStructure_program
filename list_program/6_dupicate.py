'''
@Author: Shreyash More

@Date: 2023-06-09 14:32:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-09 14:32:30

@Title :  Write a Python program to remove duplicates from a list.
'''

def duplicate(arr):
    """
    Description:
        It removes duplicate element from array
    Parameter:
        Takes array as an input
    Return:
       Returns a array with distinct element
    """
    new_arr=[]
    for i in arr:
        if i not in new_arr:
            new_arr.append(i)
    if len(new_arr)>0:
        return new_arr    
    else:
        return ["no elements"]

def main():
    arrays=list(map(int,input("Enter numbers: ").split()))
    print(f" the original array is {arrays} and new array is : {duplicate(arrays)} ")
    

if __name__=="__main__":
    main()