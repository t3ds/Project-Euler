
t = int(input)

for iter in range(0,t):

    big=0;
    x = int(input())
    temp = x;

    counter = 2;

    while counter*counter<=temp:
        if temp%counter == 0 :
            temp = temp/counter
            big = counter

        else:
            counter += 1

    if(temp>big):
        big=temp

    print(int(big))