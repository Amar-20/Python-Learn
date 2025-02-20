# find the factorial of a number using while loop

number = int(input('enter your number:'))
f = 1
while number>0:
    f=f*number
    number=number-1
print(f)
