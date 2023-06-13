'''
@Author: Shreyash More

@Date: 2023-06-13 15:35:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-13 15:35:30

@Title : Write a Python program to create an array of 5 integers and display the array items.
Access individual element through indexes.
'''
import array

def main():
    my_array = array.array('i', [10, 20, 30, 40, 50])
    # Display the array items
    print("Array items:", my_array)
    # Access individual elements through indexes
    print("Element at index 0:", my_array[0])
    print("Element at index 1:", my_array[1])
    print("Element at index 2:", my_array[2])
    print("Element at index 3:", my_array[3])
if __name__=="__main__":
    main()