'''
@Author: Shreyash More

@Date: 2023-06-09 14:32:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-09 14:32:30

@Title :  Write a Python program to clone a list.
'''
def main():
    arrays=list(map(int,input("Enter numbers: ").split()))
    cloned_array=arrays
    print(f" the original array is {arrays} and the cloned array is {cloned_array} ")
    

if __name__=="__main__":
    main()