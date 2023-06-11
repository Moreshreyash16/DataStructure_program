'''
@Author: Shreyash More

@Date: 2023-06-08 15:19:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-08 15:19:30

@Title : Write a Python program to count the number of strings where the string length
is 2 or more and the first and last character are same from a given list of strings.

'''

def first_last(arr):
    """
    Description:
        It checks if  he string length  is 2 or more and the first and last character are same from a given list of strings.
    Parameter:
        arr:Takes array as an input
    Return:
       Returns a count
    """
    final_count=0
    for i in arr:
        if len(i)>2 and (i[0]==i[len(i)-1]):
            final_count+=1
    return final_count


def main():
    arrays=list(input("Enter string: ").split())
    print(f" the total number of string present are : {first_last(arrays)} ")
    

if __name__=="__main__":
    main()