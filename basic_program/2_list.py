'''
@Author: Shreyash More

@Date: 2023-06-07 21:46:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-05 21:46:30

@Title : Write a Python program which accepts a sequence of comma-separated numbers from user
and generate a list and a tuple with those numbers.
'''
def main():
    values = input("Input numbers : ")
    lists = values.split(",")
    tuples = tuple(lists)
    print('List : ',lists)
    print('Tuple : ',tuples)


if __name__=="__main__":
    main()