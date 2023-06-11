'''
@Author: Shreyash More

@Date: 2023-06-08 15:19:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-08 15:19:30

@Title : Write a Python program to lowercase first n characters in a string.
'''

def multi(arr):
    """
    Description:
        It calculate multiplication of all elements
    Parameter:
        Takes array as an input
    Return:
       Returns multiplied value
    """
    final_value=1
    for i in arr:
        final_value=final_value*i
    return final_value


def main():
    arrays=list(map(int,input("Enter numbers: ").split()))
    print(f" the multiplied value of {arrays} is : {multi(arrays)} ")
    

if __name__=="__main__":
    main()