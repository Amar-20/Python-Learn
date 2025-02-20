#  Question  Age Group categorization
#  child(<13),teenager(13-19),adult(20-59),senior(60+)

Age= int(input("Enter your age:\n"))

if Age<13:
    print('Child')
elif Age<20:
    print('Teenager')
elif Age<60:
    print('adult')
else:
    print('senior')
    