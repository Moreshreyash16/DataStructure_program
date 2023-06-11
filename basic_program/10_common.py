'''
@Author: Shreyash More

@Date: 2023-06-07 15:35:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-07 15:35:30

@Title :Write a Python program to create a histogram from a given list of integers.
'''
def common(set1,set2):
    common_element=[]
    for i in set1: #membership operator
        if i not in set2:
            common_element.append(i)
    return common_element

def main():
    first_set=("red","yellow","blue","green")
    second_set=("red","yellow","black")
    print(common(first_set,second_set))

if __name__=="__main__":
    main()