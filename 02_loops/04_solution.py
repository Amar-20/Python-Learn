# reverse a string using loop

given_string=input('Enter your string: \n')
reversed_str=''

for s in given_string:
    reversed_str = s+reversed_str
    
print(reversed_str)