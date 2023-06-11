'''
@Author: Shreyash More

@Date: 2023-06-09 21:06:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-09 21:06:30

@Title :  Write a Python program to remove duplicates from a list.
'''

def duplicate(arr):
    """
    Description:
        It removes duplicate element from array
    Parameter:
        Takes array as an input
    Return:
       Returns a array with distinct element
    """
    new_arr=[[0]*1]*len(arr)
    count=0
    for i in arr:
        temp=[]
        for j in i:
            if j not in new_arr[count]:
                if j not in temp:
                    temp.append(j)
        new_arr[count]=temp
        count+=1
        
    if len(new_arr)>0:
        return new_arr    
    else:
        return ["no elements"]

def main():
    arrays=[]
    array_lenght=int(input("How many arrays do you want"))
    for i in range(array_lenght):
        inside_arrays=list(map(int,input(f"Enter array {i} : ").split()))
        arrays.append(inside_arrays)

    print(f" the original array is {arrays} and new array is : {duplicate(arrays)} ")
    

if __name__=="__main__":
    main()