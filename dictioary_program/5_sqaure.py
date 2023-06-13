'''
@Author: Shreyash More

@Date: 2023-06-10 18:30:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-10 18:32:30

@Title : Write a Python script to generate and print a dictionary that contains a
number (between 1 and n) in the form (x, x*x).

'''
def custom(n):
    my_dict={}
    for i in range(1,n+1):
        my_dict[i]=i*i
    return my_dict
def main():
    count=int(input("Enter a range : "))
    print(f"The dictionary is : {custom(count)}")
if __name__=="__main__":
    main()

 

 
