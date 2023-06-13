'''
@Author: Shreyash More

@Date: 2023-06-10 18:30:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-10 18:32:30

@Title : Write a Python program to count

'''
def count_list_items(dictionary):
    """
    Description:
        Count the number of items in a list that is a dictionary value.
    Parameter:
        dictionary : The dictionary containing the list value.

    Returns:
        The total number of items in the list.

    """
    count = 0

    for value in dictionary.values():
        if isinstance(value, list):
            count += 1

    return count


def main():
    my_dict = {
    'key1': [1, 2, 3],
    'key2': 'value',
    'key3': [4, 5, 6, 7]
    }
    result = count_list_items(my_dict)
    print('Total number of lists in the dictionary:', result)
if __name__=="__main__":
    main()

 

 
