
t = int(input)

for i in range(0,t):
    flag = False
    limit = int(input())

    for i in range(int(limit/1000),0,-1):
        if flag == True:
            break
        palin = i*1000 + int(str(i)[::-1])

        if palin >= limit :
            continue

        for iter in range(100,1000):
            if palin % iter == 0:
                if 100 <= int(palin / iter) <= 999:
                    flag = True
                    break

                else:
                    continue


    print(palin)