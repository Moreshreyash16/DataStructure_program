'''
@Author: Shreyash More

@Date: 2023-06-10 18:30:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-10 18:32:30

@Title : Write a Python program to remove a key from a dictionary.

'''
def main():
    my_dict = {'c': 3,'a': 1,'d': 4,'b': 2}
    print(f"The dictionary is : {my_dict}")
    key=input("Enter key you want to delete : ")
    if key in my_dict: 
        del my_dict[key]
    print(f"The dictionary after deletion is : {my_dict}")
if __name__=="__main__":
    main()

 

 
