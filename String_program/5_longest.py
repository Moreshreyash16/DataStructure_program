'''
@Author: Shreyash More

@Date: 2023-06-07 22:39:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-07 22:39:30

@Title : Write a Python function that takes a list of words and returns the length of the longest'''

def long(arr):
    """
    Description:
        It takes array of string and return longest string
    Parameter:
        Takes array as a input 
    Return:
       Returns string
    """
    max=0   # it stores the length of longest string
    for i in arr:
        if len(i)>max:
            string=i
            max=len(i)

    return string

def main():
    stri=list(input("Enter a strings in one line with space between : ").split())
    print(f" the longest string is : {long(stri)} ")


if __name__=="__main__":
    main()