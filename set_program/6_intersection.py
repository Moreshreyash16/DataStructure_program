'''
@Author: Shreyash More

@Date: 2023-06-10 10:10:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-10 10:10:30

@Title : Write a Python program to create an intersection of sets.

'''
def intersection(input_set1,input_set2):
    """
    Description:
        It finds the intersection of set
    Parameter:
        input_set1:Takes set as input
        input_set1:Takes set as input
    Return:
       Returns a set contaning intesection  value
    """
    intersection_elements=[]
    for i in input_set1:
        if i in input_set2:
            intersection_elements.append(i)
    intersection_elements=set(intersection_elements)
    return intersection_elements


def main():
    user_set_1=set(input("Enter values for set1 : ").split())
    user_set_2=set(input("Enter values for set2 : ").split())
    print(f"intersection of set1 and set2 is :{intersection(user_set_1,user_set_2)}")


if __name__=="__main__":
    main()