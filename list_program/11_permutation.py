'''
@Author: Shreyash More

@Date: 2023-06-09 14:32:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-09 14:32:30

@Title :    Write a Python function that takes two lists and returns True if they have at
least one common member.

'''
from itertools import permutations

def permutation_of_lst(arr):
    """
    Description:
        It find permutaion of list.
    Parameter:
        Takes two array as input 
    Return:
       Returns a list of all combination
    """
    permutate=list(permutations(arr,3))
    return permutate

def main():
    arrays=list(map(int,input("Enter numbers: ").split()))

    print(permutation_of_lst(arrays,))
    

if __name__=="__main__":
    main()