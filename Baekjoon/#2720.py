T = int(input())
for i in range(T) :
    mny = int(input())
    a = mny // 25
    b = (mny - a * 25) // 10
    c = (mny - a * 25 - b * 10) // 5
    d = mny - a * 25 - b * 10 - c * 5
    print(a, b, c, d)