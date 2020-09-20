import math
def rumus_abc (a, b, c):
    x_1 =(-b + math.sqrt(math.pow(b,2) -4*a*c))/(2*a)

    x_2 =(-b - math.sqrt(math.pow(b,2) -4*a*c))/(2*a)

    print (x_1)
    print (x_2)

rumus_abc(1,2,1)
rumus_abc(2,-5,-3)
