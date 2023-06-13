'''
@Author: Shreyash More

@Date: 2023-06-10 10:10:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-10 10:10:30

@Title : Write a Python program to diffrence an set diffrence.

'''

def main():
    user_set_1=set(input("Enter values for set1 : ").split())
    user_set_2=set(input("Enter values for set2 : ").split())
    print(f"set diffrence of set1 and set2 is :{user_set_1-user_set_2}")


if __name__=="__main__":
    main()