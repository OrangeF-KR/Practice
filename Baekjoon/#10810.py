N, M = map(int, input().split())
balls = [0 for _ in range(N)]

for i in range(M) :
    a, b, c = map(int, input().split())
    for j in range(a, b+1) :
        balls[j-1] = c
# 리스트 안에서 넣고 빼고 하는 작업을 보여줌
for k in range(N) :
    print(balls[k],end=' ')
# 뒤에 띄어쓰기를 통한 배열
'''
N, M = map(int, input().split())
basket = [0] * (N+1)

for _ in range(M):
    i, j, k = map(int, input().split())
    for n in range(i, j+1):
        basket[n] = k 

for i in range(1, N+1):
    print(basket[i], end = ' ')
'''
