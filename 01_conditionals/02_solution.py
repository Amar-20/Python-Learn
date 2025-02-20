# Movie tickets priced based on age
# $12 for adults(18yr and over), $8 for children. every one gets a $2 discount on wednesday.


Age=int(input('Enter your age:\n'))
day='wednesday'

# price=0
# if Age<18:
#     price=8
# else:
#     price=12

# if day=='wednesday':
#     price=price-2

# print(f'you will be charged {price} dollers')

'''Else we can aslo solve this using'''

price=12 if Age>18 else 8  #short form
if day== 'wednesday':
    price-=2

print(f'Ticket price for you is {price} dollers')