'''
@Author: Shreyash More

@Date: 2023-06-10 11:00:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-10 11:00:30

@Title : Write a Python program to clear in a set.

'''
def main():
    user_set=set(input("Enter values : ").split())
    print(f"The set is {user_set}")
    user_set.clear()
    print(f"The empty set  is {user_set}")


if __name__=="__main__":
    main()