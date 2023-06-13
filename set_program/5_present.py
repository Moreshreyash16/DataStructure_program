'''
@Author: Shreyash More

@Date: 2023-06-10 10:10:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-10 10:10:30

@Title : Write a Python program to check element in a set.

'''
def check(input_set,value):
    """
    Description:
        It check if element is present in set
    Parameter:
        input_set:Takes set as input
        value:Takes a value as input
    Return:
       Returns a boolean value
    """
    if value in input_set:
        return True
    else:
        return False


def main():
    user_set=set(input("Enter values : ").split())
    print(f"The set is {user_set}")
    value=input("Enter value to check : ")
    print(f"{check(user_set,value)}")


if __name__=="__main__":
    main()