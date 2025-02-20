# Password checker
# check if password is weak, Medium or strong.(criteria -<6(weak),6-10(medium),>10(strong))

password=input(f'Enter your password: \n')

if len(password) <6 :
    print('Weak password')
elif len(password)<10:
    print('Strong password')

elif len(password)>10:
    print('strong password')
