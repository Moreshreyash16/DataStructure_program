'''
@Author: Shreyash More

@Date: 2023-06-09 21:06:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-09 21:06:30

@Title :  Write a Python program to split a list based on first character of word.

'''


def main():
    arrays=input("Enter word: ")
    split_word=arrays[0][0]
    print(split_word)
    print(arrays.split(split_word))
    

if __name__=="__main__":
    main()