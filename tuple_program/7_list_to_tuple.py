'''
@Author: Shreyash More

@Date: 2023-06-9 23:10:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-09 23:10:30

@Title :  Write a Python program to convert a list to a tuple.


'''

def main():
    user_list=list(input("Enter numbers: ").split())
    new_tuple=tuple(user_list)
    print(f"the list is {user_list} and the tuple is {new_tuple} ")
    

if __name__=="__main__":
    main()