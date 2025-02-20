# Determine if a year is a leap year.
# any year that is evenly divisible by 4 is a leap year, but not by 100 unless by 400.

Year=int(input('Enter the year :\n'))

if (Year%4==0)or (Year%400 ==0 and Year%100 !=0):
    print('Year is leap year')

else:
    print('no leap year')
