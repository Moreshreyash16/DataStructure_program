'''
@Author: Shreyash More

@Date: 2023-06-07 15:35:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-07 15:35:30

@Title : Write a Python program to display the calender
'''
import calendar

def main():
    year = int(input("Input the year : "))
    month = int(input("Input the month : "))
    if year<9999 and year>999 and month>0 and month<13:
        print(calendar.month(year, month))
    else:
        print("Emter valid month or year")

if __name__=="__main__":
    main()