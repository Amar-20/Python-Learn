# Gread calculator
# Assign a letter grade based on a student's score:
# A(90-100), B(80-89), C(70-79), D(60-69), F(below 60)

score =int(input('enter your score:\n'))
if score>100:
    print('re-enter the correct score')
    exit()

if score >=90:
    print("Grade A")
elif score>=80:
    print('Grade B')
elif score>=70:
    print('grade C')
elif score>=60:
    print('grade D')
else:
    print('Grade F')