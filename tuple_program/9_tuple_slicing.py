'''
@Author: Shreyash More

@Date: 2023-06-9 23:10:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-09 23:10:30

@Title : Write a Python program to slice a tuple.

'''
def main():
    tup=tuple(input("Enter values : ").split())
    start=int(input("Enter start index for slicing : "))
    stop=int(input("Enter stop index for slicing: "))
    print(f"{tup[start:stop]}")

if __name__=="__main__":
    main()