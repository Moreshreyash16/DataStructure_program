'''
@Author: Shreyash More

@Date: 2023-06-07 12:35:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-07 :35:30

@Title : Write a Python program which accepts the user's first and last name and print them in
reverse order with a space between them.
'''
def main():
    first_name=input("Enter first name : ")
    last_name=input("Enter last name : ")
    print(f"{first_name[::-1]} {last_name[::-1]}")

if __name__=="__main__":
    main()