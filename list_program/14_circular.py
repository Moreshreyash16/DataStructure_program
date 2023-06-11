'''
@Author: Shreyash More

@Date: 2023-06-09 14:32:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-09 14:32:30

@Title :  . Write a Python program to Check whether two lists are circularly identical.

'''
def are_lists_circularly_identical(list1, list2):
    """
    Description:
        Check whether two lists are circularly identical.
    Parameters:
    - list1 : The first list.
    - list2 : The second list.
    
    Return:
     True if the lists are circularly identical, False otherwise.
    """
    if len(list1) != len(list2):
        return False

    # Double the first list to handle circular comparison
    list1_extended = list1 + list1

    for i in range(len(list1)):
        circular_equal = True
        for j in range(len(list2)):
            if list1_extended[i + j] != list2[j]:
                circular_equal = False
                break
        if circular_equal:
            return True

    return False


def main():
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 1, 2, 3]
    print(are_lists_circularly_identical(list1, list2))  # Output: True

    list3 = [1, 2, 3, 4, 5]
    list4 = [5, 4, 3, 2, 1]
    print(are_lists_circularly_identical(list3, list4))  # Output: False


if __name__ == "__main__":
    main()
