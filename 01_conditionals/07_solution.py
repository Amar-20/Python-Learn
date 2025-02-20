# Coffee Customization
# Customize the order: 'Small', 'Medium' or 'Large' with an option for 'extra shot' of espresso.

coffee_sizes={'small','medium','large'}
Extra_shot={'yea','no'}

while True:
    user_input = input(f'Enter the size of Coffee{coffee_sizes}').strip().lower()
    if user_input in coffee_sizes:
        
        while True:
            user_shot=input(f'Enter if you need shot{Extra_shot}').strip().lower()
            if user_shot == 'yea':
                print(f'Here is your {user_input} coffee with extra shot of expresso')
            else:
                print(f'Here is your {user_input}coffee')
            break

    else:
        print('Invalid')

