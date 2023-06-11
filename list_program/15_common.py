'''
@Author: Shreyash More

@Date: 2023-06-09 14:32:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-09 14:32:30

@Title : Write a Python program to find common items from two lists.


'''

def common_ele(arr_1,arr_2):
    """
    Description:
        It find common elements.
    Parameter:
        Takes two array as input 
    Return:
       Returns a array of common elements
    """
    common_elements=[]
    for i in arr_1:
        if i in arr_2:
            common_elements.append(i)
    if len(common_elements)>0:
        return common_elements
    else:
        print("no common elements")
        return 0    

def main():
    arrays=list(map(int,input("Enter numbers: ").split()))
    arrays_2=list(map(int,input("Enter numbers: ").split()))
    print(f"The common element are {common_ele(arrays,arrays_2)}")
    

if __name__=="__main__":
    main()