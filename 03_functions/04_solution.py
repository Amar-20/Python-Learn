# creata a function that returns both area and circumference of a circle given it radius.
import math
def cir_status(radius):
     area = (math.pi*radius**2)
     cir= (2*math.pi*radius)
     return area,cir
result =cir_status(3)
print(result)
