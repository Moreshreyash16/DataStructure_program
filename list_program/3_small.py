'''
@Author: Shreyash More

@Date: 2023-06-08 15:13:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-08 15:13:30

@Title : Write a Python program to get the smallest number from a list.

'''


def main():
    arrays=list(map(int,input("Enter numbers: ").split()))
    print(f" the smallest elemnt of {arrays} is : {min(arrays)} ")


if __name__=="__main__":
    main()