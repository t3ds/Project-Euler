import math
def sum_squared(x):

    return math.pow(x*((x + 1)/2),2)

def sum_of_squares(x):

    return x*(x + 1)*((2*x + 1)/6)

t = int(input())

for i in range(0,t):
    x = int(input())

    print(int(sum_squared(x)-sum_of_squares(x)))

