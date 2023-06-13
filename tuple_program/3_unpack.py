'''
@Author: Shreyash More

@Date: 2023-06-9 23:10:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-09 23:10:30

@Title : Write a Python program to unpack a tuple in several variables.

'''
def main():
    tup=tuple(input("Enter values : ").split())
    var1,var2,var3=tup
    print(f" the tuple variable is: {var1} {var2} {var3} ")


if __name__=="__main__":
    main()