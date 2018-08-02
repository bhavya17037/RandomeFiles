def countPairs(c,N,s):

    a = 0
    b = 0
    num = 0

    for x in range(c * N):
        if s[x] == 'a':
            a += 1
        else:
            b += 1

        if a > b:
            num += 1

    return num

T = int(raw_input())

for z in range(T):
    s1 = raw_input().split()
    s = s1[0]
    n = int(s1[1])
    N = len(s)


    if n == 1:
        print(countPairs(1,N,s))
    elif n == 2:
        print(countPairs(2,N,s+s))
    else:

        B = 0

        for i in range(N):
            if s[i] == 'b':
                B += 1


        i = 0
        start = 0
        a = 0
        b = 0
        num = 0
        index = 0
        while True:
            if index >= N:
                index = 0

            if s[index] == 'a':
                a += 1
            else:
                b += 1

            if a - b > B:
                while index < n:
                    index += 1
                    num += 1
                break
            else:
                if a > b:
                    num += 1
                index += 1


        print(num + (N * n) - index)