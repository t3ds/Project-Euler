
def calc_fibo(limit):
    fibo=[0,2]
    i=0
    sum=0

    while fibo[i]<=limit:
        sum+=fibo[i]
        fibo[i]= 4*fibo[1-i]+fibo[i]
        i=1-i

    return sum
t = int(input())

for i in range(0,t):
    lim = int(input())
    print(calc_fibo(lim))

#0 1 1 2 3 5 8 13 21 34
#total=44
#i=0 [0 2] 2
#i=0 [8 2] 2
#i=1 [8 34] 4