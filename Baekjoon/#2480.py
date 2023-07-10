a, b, c = map(int, input().split())
lst = [a, b, c]

if a == b == c :
    print(10000 + a*1000)
elif a != b != c :
    print((max(lst)*100))
else :
    if a == b or a == c :
        print(1000 + a*100)
    elif a == c :
        print(1000 + a*100)
    else :
        print(1000 + b*100)
'''
a, b, c = map(int, input().split())
if a == b == c:
    print(10000 + a*1000)
elif a == b or a == c:
    print(1000 + a*100)
elif b == c:
    print(1000 + b*100)
else:
    print(max(a, b, c)*100)'''
