'''
@Author: Shreyash More

@Date: 2023-06-09 14:32:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-09 14:32:30

@Title :   Write a Python program to print a specified list after removing the 0th, 4th and
5th elements.

'''
def remove_specific(arrays,index):
    """
    Description:
        It removes specific value
    Parameter:
        Takes one array as input one is array of element and another is of index
    Return:
       Returns a modified array
    """
    index.sort()
    index.reverse()             
    for i in index:
        arrays.pop(i)
    return arrays


def main():
    arrays=list(input("Enter words: ").split())
    print(arrays)
    index_of_list=list(map(int,input("Enter index: ").split()))
    print(f" the original array is {arrays} and new array is : {remove_specific(arrays,index_of_list)} ")

if __name__=="__main__":
    main()