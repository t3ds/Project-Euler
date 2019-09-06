
def compute_gcd(a,b):

    while b :
        a,b = b,(a % b)
    return a

def lcm(a,b):
    return a*(b/compute_gcd(a,b))

t=int(input())

for i in range(0,t):
    result = 1;
    limit = int(input())

    for j in range(2,limit+1):
        result = lcm(result,j)

    print(int(result))