'''
@Author: Shreyash More

@Date: 2023-06-10 18:30:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-10 18:32:30

@Title : Write a Python program to print in table format

'''
def main():
    my_dict = {(0, 0): 'Shreyash', (0, 1): 2, (0, 2): 'AI',
         (1, 0): 'Anish', (1, 1): 3, (1, 2): 'Web devlopment',
         (2, 0): 'Bhoomik', (2, 1): 5, (2, 2): 'Full stack'
         }

    print(" NAME ", " DURATION ", "  COURSE ")
    for i in range(3):
        for j in range(3):
            print(my_dict[(i, j)], end='   ')
        print()
if __name__=="__main__":
    main()
#tabulate