'''
@Author: Shreyash More

@Date: 2023-06-10 18:30:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-10 18:32:30

@Title : Write a Python program to add value in a dict.

'''
def main():
    my_dict = {'c': 3,'a': 1,'d': 4,'b': 2}
    key=input("Enter key : ")
    value=input("Enter value : ")
    my_dict[key]=value
    print(f"The dictionary is : {my_dict}")
if __name__=="__main__":
    main()

 

 
