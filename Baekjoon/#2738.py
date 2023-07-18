N, M = map(int, input().split())
A, B = [], []

for i in range(N) :
    i = list(map(int,input().split()))
    A.append(i)

for j in range(N) :
    j = list(map(int,input().split()))
    B.append(j)

for k in range(N) :
    for l in range(M) :
        print(A[k][l] + B[k][l], end=' ')
    print()
