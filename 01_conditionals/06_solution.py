# Transportation mode selection
# choose a mode of transportation based on the distance(eg: <3km: walk,3-15km:Bike,>15km:car)

km = int(input('Enter the kilo meters: '))

if km<3:
    mode='Walk'
elif km>=3 and km<=15:
    mode='Bike'
else:
    mode='Car'

print(mode)