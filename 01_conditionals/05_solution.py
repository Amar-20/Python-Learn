# Weather activity suggestion
# problem: suggest an activity based on the weather(eg: sunny- go for walk, rainy- Read a book, Snowny- built Snowman)


weather={'Sunny','Snowny','Rainy'}

while True:
    weather_input = input(f'Enter the weather {weather}:').strip().lower()
    if weather_input == 'sunny':
        activity='go for a walk'
        # print('Go for a walk') 
    elif weather_input == 'rainy':
        activity='Read a book'
        # print('Read a book')
    elif weather_input == 'snowny':
        activity='Built a snowman'
        # print('built a snowman')
    else:
        print('Invalid weather')
    
    print(activity)
    
