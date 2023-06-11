'''
@Author: Shreyash More

@Date: 2023-06-07 15:35:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-07 15:35:30

@Title :Write a Python program to check whether a file exists.
'''

import os

def path(pth):
    """
    Description:
        It checks if file exits or not
    Parameter:
        Takes file path as a input 
    Return:
       Returns true if file exist
    """
    file=os.path.isfile(pth)
    if(file):
        return ("File exist")
    else:
        return ("File does not exist ")


def main():
    file_path='D:/vscode/Bridgelabz/data_structure/basic_program/3_index.py'
    print(path(file_path))
    file_path='D:/vscode/Bridgelabz/data_structure/basic_program/3_index.'
    print(path(file_path))

if __name__=="__main__":
    main()