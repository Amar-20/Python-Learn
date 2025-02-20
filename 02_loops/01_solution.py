# counting positive numbers
#  given a list of numbers. count how many are positive numbers.
#  numbers =[1,-2,3,-4,5,6,-7,-8,9,10]

numbers=[1,-2,3,-4,5,6,-7,-8,9,10]
positive_count=0
negtive_count=0
for n in numbers:
    if n  >0:
        positive_count+=1
    else:
        negtive_count+=1
print(f'final count of positive numbers is {positive_count} and final count of negative number is {negtive_count}')
