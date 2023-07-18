N, M = map(int, input().split())

baskets = [i for i in range(1, N+1)]

for j in range(M) :
    a, b = map(int, input().split())
    baskets[a-1:b] = reversed(baskets[a-1:b]) # reserve를 바로 호출하느 방법 reservwed


print(*baskets)   # 리스트의 컨텐츠를 한 줄 띄어쓰기 하나로 프린트하는 법 print(*list)

''''
N, M = map(int, input().split())

basket = [i for i in range(1,N+1)]

for i in range(M):
    i,j = map(int, input().split())
    temp = basket[i-1:j]
    temp.reverse()
    basket[i-1:j] = temp

for i in range(N):
    print(basket[i], end = ' ')
    '''
