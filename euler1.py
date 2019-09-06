import math

def calculate(n):
    return (n*(n+1))/2

t = int(input())

for i in range(0,t):
    lim = int(input())
    three = int(3*calculate(math.floor((lim-1)/3)))
    five = int(5*calculate(math.floor((lim-1)/5)))
    fifteen = int(15*calculate(math.floor((lim-1)/15)))
    print(three,five,fifteen)

    print(three+five-fifteen)


