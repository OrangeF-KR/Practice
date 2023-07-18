N, M = map(int, input().split())

baskets = [ 0 for _ in range(N)]

for k in range(N) :
    baskets[k] = k+1

for i in range(M) :
    a, b = map(int, input().split())
    baskets[a-1],baskets[b-1] = baskets[b-1],baskets[a-1]

for j in range(N) :
    print(baskets[j], end=' ')

'''
N,M = map(int, input().split())

basket = [i for i in range(1,N+1)]

for i in range(M):
    i,j = map(int, input().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

for i in range(N):
    print(basket[i], end = ' ')
'''

'''
N,M = map(int, input().split())

basket = [i for i in range(1,N+1)]
temp = 0

for i in range(M):
    i,j = map(int, input().split())
    temp = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = temp

for i in range(N):
    print(basket[i], end = ' ')
    '''





