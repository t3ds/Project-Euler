import math

big = 0;
def is_prime(n):
    for i in range(3,math.ceil(math.sqrt(n))):
        #if i&1 == 0 :
         #   continue

        #if:
            if n%i == 0 :
                return False


    return True

x = int(input())

if x==2:
    big=2;

else:
    for i in range(3,x,2):
        if i&1:
            #print(i)
            if is_prime(i) and x%i == 0:
                big = i;
                #print(big)

print(big)
