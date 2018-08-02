t = int(raw_input())
for i in range(t):
    s = list(map(int,raw_input().split()))
    n = s[0]
    w = s[1]

    a = 0

    if w > -10 and w < 10:
        if w >= 0:
            a = (pow(10,n-2,1000000007) * (9 - w)) % 1000000007
        else:
            a = (pow(10,n-2,1000000007) * (9 + w + 1)) % 1000000007
    else:
        a = 0

    print(a)