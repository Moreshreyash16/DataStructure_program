'''
@Author: Shreyash More

@Date: 2023-06-07 17:35:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-07 17:35:30

@Title :Write a Python program to give all files
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
    dir_list = os.listdir(pth)
    return dir_list


def main():
    file_path='D:/vscode/Bridgelabz/data_structure/basic_program'
    print(path(file_path))

if __name__=="__main__":
    main()