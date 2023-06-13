'''
@Author: Shreyash More

@Date: 2023-06-10 10:10:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-10 10:10:30

@Title : Write a Python program to create an union of sets.

'''
def intersection(input_set1,input_set2):
    """
    Description:
        It finds the union of set
    Parameter:
        input_set1:Takes set as input
        input_set1:Takes set as input
    Return:
       Returns a set contaning union value
    """

    for i in input_set2:
        input_set1.add(i)
    return input_set1


def main():
    user_set_1=set(input("Enter values for set1 : ").split())
    user_set_2=set(input("Enter values for set2 : ").split())
    
    print(f"union of set1 and set2 is :{intersection(user_set_1,user_set_2)}")


if __name__=="__main__":
    main()