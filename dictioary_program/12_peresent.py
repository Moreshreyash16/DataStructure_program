'''
@Author: Shreyash More

@Date: 2023-06-10 18:30:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-10 18:32:30

@Title :  Python program to check multiple keys exists in a dictionary

'''
def check_multiple_keys(dict,keys):
    """
    Description :
            This function checks if the keys are present in the dictionary or not.
    Parameters :
            dict : dictionary of elements from input.
            keys : key list.
    Returns : 
            boolean
    """
    for key in keys:
        if key not in dict:
            return False
    return True

def main():
    dict_elements = {1:'batman',2:'superman',3:'spiderman',4:'captain-america'} 
    keys =list(map(int,input("Enter key to check")).split())
    result = check_multiple_keys(dict_elements, keys)
    if result == True:
        print("keys exist ")
    else:
        print("keys does not exist dictionary.")


if __name__ == "_main_":
    main()