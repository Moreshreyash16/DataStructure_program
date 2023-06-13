'''
@Author: Shreyash More

@Date: 2023-06-07 23:10:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-07 23:10:30

@Title : Write a Python program to get a string and to convert lower to upper
'''

def case_convert(string):
    """
    Description:
        It convert lower to upper case
    Parameter:
        Takes string as a input 
    Return:
       Returns modiffied string
    """
    new_string=""
    for i in string:
        if i==i.upper():
            new_string+=i.lower()
        else:
            new_string+=i.upper()
    return new_string

def main():
    str=input("Enter a string : ")
    print(f" {case_convert(str)} ")


if __name__=="__main__":
    main()