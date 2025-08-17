import math

def function(a, b):
    x, y = 0, 0
    power = 50

    x1 = 2**(a - x)
    y1 = 2**(b - y)

    theta = math.atan2(y1, x1)

    c = math.cos(theta) * power
    s = math.sin(theta) * power

    return(c,s)

    
result = function(5, 3)    
print(result)


    