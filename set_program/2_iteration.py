'''
@Author: Shreyash More

@Date: 2023-06-9 23:10:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-09 23:10:30

@Title : Write a Python program to iteration over sets.

'''
def main():
    user_set=set(input("Enter values : ").split())
    for i in user_set:
        print(f" the set value is : {i} ")


if __name__=="__main__":
    main()