# set a default name if user doesn't provide any.

def greet(name= 'Dear'):
    return 'Hello,'+ name+'!!'

print(greet())
print(greet('Amar'))