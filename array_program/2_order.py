'''
@Author: Shreyash More

@Date: 2023-06-13 15:35:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-13 15:35:30

@Title : Write a Python program to reverse the order of the items in the array.
'''
import array

def main():
    my_array = array.array('i', [10, 20, 30, 40, 50])
    # Reverse the order of items
    my_array.reverse()
    print("Reversed array is :", my_array)
if __name__=="__main__":
    main()