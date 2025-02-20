# find the first non-repeted char
# given a string , find the first non-repeated char

given_str=input('enter your string: \n')


for n in given_str:
   print(n)
   if  given_str.count(n) ==1:
      print(f'char:{n}')
      break  # they have asked to find only the first non-repeating char
