'''
@Author: Shreyash More

@Date: 2023-06-07 17:39:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-07 17:39:30

@Title : Write a Python program to get a string from a given string where all occurrences of its
'''

def replace(string):
    """
    Description:
        It replace the last three letter by "ing"
    Parameter:
        Takes string as a input 
    Return:
       Returns modiffied string
    """
    if len(string)>2:
        if string[-3:]=="ing":
           string+="ly" 
        else:
            string+="ing"
    return string

def main():
    str=input("Enter a string : ")
    print(f" {replace(str)} ")


if __name__=="__main__":
    main()