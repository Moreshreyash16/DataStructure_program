'''
@Author: Shreyash More

@Date: 2023-06-09 14:32:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-09 14:32:30

@Title :  Write a Python program to get the difference between the two lists.


'''

def diffrence_of_list(arr_1,arr_2):
    """
    Description:
        It find diffrence in list
    Parameter:
        Takes two array as input 
    Return:
       Returns diffrence
    """
    diffrence=0
    for i in arr_1:
        if i not in arr_2:
            diffrence+=1
    for j in arr_2:
        if j not in arr_1:
            diffrence+=1
    
    return diffrence
        
def main():
    arrays=list(map(int,input("Enter numbers for list1: ").split()))
    
    arrays_2=list(map(int,input("Enter numbers for list2: ").split()))
    print(type(arrays))
    # diff_array=list(arrays-arrays_2)
    # print(diff_array)
    print(f"The diffrence between two list is {diffrence_of_list(arrays,arrays_2)}")
    

if __name__=="__main__":
    main()