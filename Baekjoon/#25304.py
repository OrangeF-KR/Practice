X = int(input())
N = int(input())
Total = 0
for i in range(N) :
    a, b = map(int,input().split())
    Total += (a * b)
if X == Total :
    print("Yes")
else :
    print("No")



