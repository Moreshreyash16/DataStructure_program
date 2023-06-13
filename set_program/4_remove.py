'''
@Author: Shreyash More

@Date: 2023-06-9 23:10:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-09 23:10:30

@Title : Write a Python program to remove member(s) in a set.

'''
def main():
    user_set=set(input("Enter values : ").split())
    print(f"The set is {user_set}")
    value=input("Enter value to remove : ")
    user_set.remove(value)
    print(f"The set is {user_set}")


if __name__=="__main__":
    main()