'''
@Author: Shreyash More

@Date: 2023-06-07 17:35:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-07 17:35:30

@Title :Write a Python program to access enviromennt variable
'''
import os
def environment_variable(var):
    """
    Description : 
        This function access the environment variable.
    Parameters :
        takes a variable as a uservalue
    Return : 
        None
    """
    if var in os.environ:
        value = os.environ[var]
        print("found")
        print(value)
    else :
        print("Environment variable does not exist")


def main():
    env_var = 'USERNAME'
    environment_variable(env_var)


if __name__ == "_main_":
    main()