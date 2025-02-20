#Fruit ripness
# Determine if fruit is ripe, overripe,or unripe based on its color
# (eg: banana: Green-Unripe,Yellow- Ripe, Brown- Overripe)

allowed_fruits={'banana','apple','mango'}
allowed_colors={
    "banana":{"green":"Unripe","yellow":'Ripe',"brown":"overripe"},
    "apple":{"green":"Unripe","yellow":"Ripe","brown":"overripe"},
    "mango":{"green":"Unripe","yellow":"Ripe","brown":"overripe"}

}

while True:
    user_fruit= input(f"Enter the fruit name{allowed_fruits}: ").strip().lower()
    if user_fruit in allowed_fruits:

        while True:
            user_color=input(f"Enter the color of {user_fruit}: ").strip().lower()
            if user_color in allowed_colors[user_fruit]:
                ripeness = allowed_colors[user_fruit][user_color]
                print(f'The {user_fruit} is {ripeness}')
                break
            else:
                print("Invalid color.please try again")
        break
    else:
        print("Invalid fruit")

