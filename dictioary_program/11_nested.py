'''
@Author: Shreyash More

@Date: 2023-06-10 18:30:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-10 18:32:30

@Title : Write a Python program to create a nested dictionary

'''
def list_to_nested_dict(lst):
    """
    Description:
        This function takes a list as input and converts it into a nested dictionary of keys.

    Parameters:
        lst : The input list to be converted.

    Returns:
        A nested dictionary with keys generated from the list elements.

    """
    nested_dict = {}
    current_dict = nested_dict

    for item in lst:
        current_dict[item] = {}
        current_dict = current_dict[item]

    return nested_dict


def main():
    my_list = ['a', 'b', 'c', 'd']
    result = list_to_nested_dict(my_list)
    print(result)


if __name__ == '__main__':
    main()


 

 
