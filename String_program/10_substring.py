'''
@Author: Shreyash More

@Date: 2023-06-07 23:10:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-07 23:10:30

@Title : Write a Python program to find sub string frequency
'''

def main():
    str=input("Enter a string : ")
    sub_str=input("Enter a substring : ")
    print(f" The count of {sub_str} is {str.count(sub_str)} ")


if __name__=="__main__":
    main()