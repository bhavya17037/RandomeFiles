t = int(raw_input())
for r in range(t):

    n = int(raw_input())
    s = raw_input().split()
    s = [int(x) for x in s]

    d = {}

    for i in range(-1000,1001,1):
        d[i] = 0

    for i in range(n):
        d[s[i]] += 1

    count = 0

    for i in range(-1000,1001,1):
        if d[i] > 0:
            for j in range(i+2,1001,2):
                if j < 1001:
                    if d[j] > 0:
                        if (i+j) % 2 == 0:
                            avg = (i + j) / 2
                            if avg in d:
                                if d[avg] > 0:
                                    count += (d[i] * d[j])
        if d[i] > 1:
            f = d[i]
            count += (f * (f - 1)) / 2


    print(count)
