'''
@Author: Shreyash More

@Date: 2023-06-07 15:35:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-07 15:35:30

@Title : Write a Python program to calculate number of days between two dates.
'''
import datetime

def main():
    first_date=datetime.date(2022,8,15)
    last_date=datetime.date(2022,9,15)
    final_date=last_date-first_date
    print(f"The days between two dates are : {final_date.days} days")


if __name__=="__main__":
    main()