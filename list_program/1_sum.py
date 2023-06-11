'''
@Author: Shreyash More

@Date: 2023-06-08 15:13:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-08 15:13:30

@Title : Write a Python program to sum all the items in a list.
'''


def main():
    arrays=list(map(int,input("Enter numbers: ").split()))
    print(f" the sum of {arrays} is : {sum(arrays)} ")


if __name__=="__main__":
    main()