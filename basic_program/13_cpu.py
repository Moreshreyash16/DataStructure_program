'''
@Author: Shreyash More

@Date: 2023-06-07 17:35:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-07 17:35:30

@Title :Write a Python program to find out the number of CPUs using.
'''

import os
# Extract CPUs count

def main():
    cpu = os.cpu_count()
    print("Total CPUs count:", cpu)

if __name__=="__main__":
    main()