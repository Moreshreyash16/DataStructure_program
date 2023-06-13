'''
@Author: Shreyash More

@Date: 2023-06-07 23:10:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-07 23:10:30

@Title : Write a Python program to lowercase first n characters in a string.
'''

def n_lower(string,n):
    """
    Description:
        It prints result till specific character
    Parameter:
        Takes string as a input and the specified character
    Return:
       Returns modiffied string
    """
    new_str=""
    first=string[:n]
    new_str+=first.lower() + string[n:]
    return new_str


def main():
    str=input("Enter a string : ")
    n=int(input("Enter a number"))
    print(f" {n_lower(str,n)} ")
    

if __name__=="__main__":
    main()