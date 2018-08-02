s = list(map(int,raw_input().split()))
N = s[0]
M = s[1]
K = s[2]

A = list(map(int,raw_input().split()))
P = list(map(int,raw_input().split()))

s = ""

for i in A:
    s += str(i + K/2) + " "


print(s)
