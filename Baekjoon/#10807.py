N = int(input())
a = list(map(int, input().split()))
v = int(input())
count = 0

for i in range(N) :
    if a[i] == v :
        count += 1
    else :
        pass
print(count)
'''
N = int(input())
l = list(map(int, input().split()))
v = int(input())

print(l.count(v))
아 이런 count 기억하기
'''


