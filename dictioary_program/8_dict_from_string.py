'''
@Author: Shreyash More

@Date: 2023-06-10 18:30:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-10 18:32:30

@Title : Write a Python program to create a dictionary from a string.

'''
def conversion(user_input):
    """
    Description:
        It create a dictionary from a string.
    Parameter:
        user_input:Takes string as an input
    Return:
       Returns a dictionary
    """
    my_dict={}
    for i in user_input:
        my_dict[i]=user_input.count(i)
    return my_dict

def main():
    word=input("Enter a string: ")
    print(f"The dictionary is : {conversion(word)}")
if __name__=="__main__":
    main()

 

 
