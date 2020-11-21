import math

def quadratic_func(a, b, c):
    delta = b*b - 4*a*c
    if (delta == 0):
        x0 = -b/(2*a)
        print("the equation has one solution: ", x0)
    elif (delta > 0):
        x1 = (-b - math.sqrt(delta))/(2*a)
        x2 = (-b + math.sqrt(delta))/(2*a)
        print("the equation has two solutions: ", x1, ", ", x2)
    else:
        print("the equation has no real solutions")

quadratic_func(1,4,1)

