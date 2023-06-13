'''
@Author: Shreyash More

@Date: 2023-06-10 18:30:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-10 18:32:30

@Title : Write a Python program to find maximum and the minimum value in a set.

'''
def main():
    dict1={1:10, 2:20}
    dict2={3:30, 4:40}
    dict3={5:50,6:60}
    dict4={}
    for i in (dict1,dict2,dict3):
        print(i)
        dict4.update(i)
    
    # Print sorted dictionary
    print(f"The dictionary is : {dict4}")
if __name__=="__main__":
    main()

 

 
