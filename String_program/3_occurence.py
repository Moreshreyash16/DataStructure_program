'''
@Author: Shreyash More

@Date: 2023-06-07 17:39:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-07 17:39:30

@Title : Write a Python program to get a string from a given string where all occurrences of its
'''

def occurcence(string):
    """
    Description:
        It replace the first letter by $
    Parameter:
        Takes string as a input 
    Return:
       Returns modified string
    """
    char=string[0]
    string=string.replace(char,"$")
    char+=string[1:]
    return char

def main():
    str=input("Enter a string : ")
    print(f" {occurcence(str)} ")


if __name__=="__main__":
    main()