# Sum of even numbers
# calculate the sum of even numbers up to a given number n.

number =int(input('Enter a number: \n'))

sum=0
for n in range(1, number+1):
    if n%2==0:
        sum+=n
        print(n,end=',\n')

print(f'sum of even number is {sum}')