'''
@Author: Shreyash More

@Date: 2023-06-10 18:30:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-10 18:32:30

@Title : Write a Python program to sort value in a dictionary.

'''
def main():
    my_dict = {'c': 3,'a': 1,'d': 4,'b': 2}
    # Sorting dictionary
    sorted_dict = sorted([(key,value)for (key, value) in my_dict.items()])
    # Print sorted dictionary
    print(f"Sorted dictionary is : {sorted_dict}")
if __name__=="__main__":
    main()

 

 
