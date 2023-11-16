N = int(input())
a = list()
b = list()
for i in range(N) :
    c, d = map(int, input().split())
    a.append(c)
    b.append(d)
print((max(a)-min(a))*(max(b)-min(b)))


