# multiplication table up to 10 , skip fifth iteration.

number =int(input('Enter a number'))
for i in range(1,11):
    if i==5:
        continue
    print(number,'X',i,'=',number*i)
   