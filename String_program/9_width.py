'''
@Author: Shreyash More

@Date: 2023-06-07 23:10:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-07 23:10:30

@Title : Write a Python program to get a string and to convert lower to upper
'''
import textwrap

def formatted_text(plain_text):
    """
    Description : 
            This function formats text to 50 characters per line using 'textwrap.fill' function.
    Parameters : plain_text - input text
    Return :
            returns nothing 
            print formatted text.
    """
    print(textwrap.fill(plain_text, width=10))

# main
def main():
    text = '''
    Python: Powerful, versatile, and beginner-friendly.
    It promotes code readability, offers a vast ecosystem of libraries, 
    and has a strong community. Boost your productivity with Python!
    '''
    formatted_text(text)


if __name__ == "_main_":
    main()