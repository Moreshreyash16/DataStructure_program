'''
@Author: Shreyash More

@Date: 2023-06-07 12:35:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-07 22:19:30

@Title : Write a Python program which accepts the user's first and last name and print them in
reverse order with a space between them.
'''
def main():
    first_name=input("Enter first name : ")
    # print(f"the reverse of {first_name} is {first_name[::-1]}")
    name=""
    for i in first_name:
        name=i + name
    print(name)
if __name__=="__main__":
    main()