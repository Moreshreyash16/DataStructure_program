'''
@Author: Shreyash More

@Date: 2023-06-09 14:32:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-09 14:32:30

@Title :  . Write a Python program to append a list to the second list.

'''

def combine_list(arr_1,arr_2):
    """
    Description:
        It append second list to first list
    Parameter:
        Takes two array as input 
    Return:
       Returns first list
    """
    for i in arr_2:
        arr_1.append(i)
    return arr_1
        
def main():
    arrays=list(map(int,input("Enter numbers for list1: ").split()))
    arrays_2=list(map(int,input("Enter numbers for list2: ").split()))
    print(f"The newlist {combine_list(arrays,arrays_2)}")
    

if __name__=="__main__":
    main()