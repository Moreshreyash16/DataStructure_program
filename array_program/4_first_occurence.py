'''
@Author: Shreyash More

@Date: 2023-06-13 15:35:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-13 15:35:30

@Title :Write a Python program to remove the first occurrence of a specified element from an
array
'''
import array

def main():
    my_array = array.array('i', [10, 20, 30, 20, 40, 20, 50])
    # Take input from the user for the element to remove
    element = int(input("Enter the element to remove from the array: "))
    if element in my_array:
        index = my_array.index(element)
        my_array.pop(index)
        # Display the modified array
        print("Modified array:", my_array)
    else:
        print("Element not found in the array.")
if __name__=="__main__":
    main()