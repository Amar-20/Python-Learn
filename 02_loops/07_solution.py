# ask the user to enter the number until he 'enter a number between  1 and 10' 

while True:
    number= int(input('enter value between 1 and 10'))
    if number>1 and number<10:
        print('Thanks')
        break
    else:
        print('invalid,Enter your input again')