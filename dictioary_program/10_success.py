'''
@Author: Shreyash More

@Date: 2023-06-10 18:30:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-10 18:32:30

@Title : Write a Python program to count the values associated with key in a
dictionary.
'''
def count_success(data):
    """
    Description:
        Count the number of dictionaries in a list that have the key 'success' with a value of True.
    Parameters:
        data : A list of dictionaries.

    Return:
        The count of dictionaries where 'success' is True.
    """
    count = 0
    for d in data:
        if d.get('success') == True:
            count += 1
    return count


def main():
    data = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
    success_count = count_success(data)
    print("Count of dictionaries with success as True:", success_count)


if __name__ == '__main__':
    main()



 

 
