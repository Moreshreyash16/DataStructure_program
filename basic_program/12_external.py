import os
'''
@Author: Shreyash More

@Date: 2023-06-07 17:35:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-07 17:35:30

@Title :Write a Python program to check whether a file exists.
'''
def ext_command(cmd):
    """
    Description : 
                This function executes given system commands.
    Parameters : 
            cmd: taking user input 
    Return : 
            returns the  system commands
    """
    return os.system(cmd)


def main():
    command = input("Enter command: ")
    output=ext_command(command)
    print(output)

if __name__ == "_main_":
    print("hello")
    main()