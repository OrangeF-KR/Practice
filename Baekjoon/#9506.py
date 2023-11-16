
while :
    n = int(input())
    num = list()
    for i in range(1, n+1) :
        if n % i == 0 :
            num.append(i)
        else :
            continue
    cnt = 0
    for i in range(len(num)-1) :
        cnt += num[i]
    if cnt == n :
        print(f'{n} = ')