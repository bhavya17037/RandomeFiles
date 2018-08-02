N = input()
c = raw_input().split()
c = [int(x) for x in c]
t = raw_input().split()
t = [int(x) for x in t]

threes = []
ones = []
twos = []

for i in range(N):
    if t[i] == 3:
        threes.append(c[i])
    elif t[i] == 2:
        twos.append(c[i])
    else:
        ones.append(c[i])

sums1 = []

a = len(ones)
b = len(twos)
c = len(threes)

if(a == 0 or b == 0):
    print(min(threes))
else:
    for i in range(a):
        for j in range(b):
            sums1.append(ones[i] + twos[j])
    if c == 0:
        print(min(sums1))
    else:
        n = min(threes)
        m = min(sums1)

        print(min(m,n))



