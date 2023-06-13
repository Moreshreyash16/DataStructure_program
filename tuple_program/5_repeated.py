'''
@Author: Shreyash More

@Date: 2023-06-9 23:10:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-09 23:10:30

@Title :  Write a Python program to find the repeated items of a tuple.


'''

def repeat(tuples):
    """
    Description:
        It gives duplicate element from tuple
    Parameter:
        tuples:Takes array as an tuple
    Return:
       Returns a repeated element
    """
    duplicate=[]
    for i in tuples:
        if tuples.count(i)>1 and i not in duplicate:
            duplicate.append(i)
    duplicate=tuple(duplicate)
    return duplicate


def main():
    user_tuple=tuple(map(int,input("Enter numbers: ").split()))
    print(f" the original array is {user_tuple} and repeated element are : {repeat(user_tuple)} ")
    

if __name__=="__main__":
    main()