'''
@Author: Shreyash More

@Date: 2023-06-07 17:39:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-07 17:39:30

@Title : Write a Python program to count the number of characters
'''
def frequency(string):
    """
    Description:
        It counts the frequency of letters and store in dictionary
    Parameter:
        Takes string as a input 
    Return:
       Returns dictionary
    """
    final={}
    count=0
    # new_string=string.lower()

    for i in string.lower():
        for j in string.lower():
            if i==j:
                count+=1
        final[i]=count
        count=0
    return final


def main():
    str=input("Enter a string : ")
    print(f" {frequency(str)} ")


if __name__=="__main__":
    main()