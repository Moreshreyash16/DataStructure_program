'''
@Author: Shreyash More

@Date: 2023-06-08 15:19:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-08 15:19:30

@Title :  Write a Python program to get a list, sorted in increasing order by the last
element in each tuple from a given list of non-empty tuples.

'''

def last(n): 
    """
    Description : This function returns n with last index.
    Parameters : 
            n : tuples in list
    Retrun : 
            last element
    """
    return n[-1]

def sort(arr):
    """
    Description:
        It sorts by the second element
    Parameter:
        arr:Takes array as an input
    Return:
       Returns a sorted array
    """
    return sorted(arr, key=last)    



def main():
    # arrays=list(tuple(map(int,input("Enter numbers: ").split())))
    arrays=[(1,5),(2,3)]
    print(arrays[0][1])
    print(f" the sorted elemnt of {arrays} is : {sort(arrays)} ")
    

if __name__=="__main__":
    main()