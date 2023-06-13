'''
@Author: Shreyash More

@Date: 2023-06-13 15:35:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-13 15:35:30

@Title : Write a Python program to get the number of occurrences of a specified element in an
array.
'''
import array

def main():
    my_array = array.array('i', [10, 20, 30, 20, 40, 20, 50])
    # Take input from the user for the element to count occurrences
    element = int(input("Enter the element to count occurrences: "))
    # Count the number of occurrences of the specified element
    count = my_array.count(element)
    print(f"Number of occurrences of {element} in the array:{count}")
if __name__=="__main__":
    main()