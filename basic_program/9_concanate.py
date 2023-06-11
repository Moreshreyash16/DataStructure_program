'''
@Author: Shreyash More

@Date: 2023-06-07 15:35:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-07 15:35:30

@Title :Write a Python program to concatenate all elements in a list into a string and return it.
'''
def concant(arr):
    """
    Description:
        It concatenate all elements in a list into a string
    Parameter:
        Takes array as a input 
    Return:
       Returns concatenated value
    """
    final=" "
    for i in arr:
        final+=" "+str(i)
    print(type(final))
    return final
def main():
    array=["S","D","d",5]
    print(concant(array))
if __name__=="__main__":
    main()