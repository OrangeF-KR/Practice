A, B = map(int, input().split())
C = int(input())
D = B + C
if D >= 60 :
    A += (D // 60)
    D = D - 60 * (D // 60)
    if A >= 24 :
        A = A - 24

print(A, D)
'''
A,B=map(int,input().split())
C=int(input())
print((A+((B+C)//60))%24,(B+C)%60)
'''