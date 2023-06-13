'''
@Author: Shreyash More

@Date: 2023-06-10 10:10:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-10 10:10:30

@Title : Write a Python program to create an union of sets.

'''
def symetric_diffrence(input_set1,input_set2):
    """
    Description:
        It finds the diffrence of two set
    Parameter:
        input_set1:Takes set as input
        input_set1:Takes set as input
    Return:
       Returns a set contaning symetric set diffrence
    """
    value1=input_set1-input_set2
    value2=input_set2-input_set1
    final_set=list(value1)+list(value2)
    return set(final_set)

def main():
    user_set_1=set(input("Enter values for set1 : ").split())
    user_set_2=set(input("Enter values for set2 : ").split())
    print(f"set diffrence of set1 and set2 is :{symetric_diffrence(user_set_1,user_set_2)}")


if __name__=="__main__":
    main()