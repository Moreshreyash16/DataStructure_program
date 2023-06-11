'''
@Author: Shreyash More

@Date: 2023-06-09 14:32:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-09 14:32:30

@Title :   Write a Python program to find the list of words that are longer than n from a
given list of words.

'''

def fixed_size(arr,n):
    """
    Description:
        It find string that are greater than n lenght
    Parameter:
        Takes array  and a n as an input
    Return:
       Returns a array with distinct element
    """
    
    for i in arr:
        if len(i)<n:
            arr.remove(i)
    return arr

def main():
    arrays=list(input("Enter words: ").split())
    number=int(input("Enter a size: "))
    print(f" the original array is {arrays} and new array is : {fixed_size(arrays,number)} ")
    

if __name__=="__main__":
    main()