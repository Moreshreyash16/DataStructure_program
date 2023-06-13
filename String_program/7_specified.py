'''
@Author: Shreyash More

@Date: 2023-06-07 23:03:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-07 23:03:30

@Title : Write a Python program to get a string from a given string where all occurrences of its
'''

def specific(string,char):
    """
    Description:
        It prints result till specific character
    Parameter:
        Takes string as a input and the specified character
    Return:
       Returns modiffied string
    """
    new_str=""
    count=0
    for i in string:
        if i==char:
            new_str+=string[:count]
            break
        count+=1
    return new_str

def main():
    str=input("Enter a string : ")
    val=input("Enter a value : ")
    print(f" {specific(str,val)} ")


if __name__=="__main__":
    main()