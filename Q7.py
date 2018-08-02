T = int(raw_input())

for r in range(T):
    N = int(raw_input())
    initial = list(map(int,raw_input().split()))
    final = list(map(int,raw_input().split()))

    isPossible = True

    for i in range(N):
        if final[i] > initial[i]:
            isPossible = False
            break

    if not isPossible:
        print(-1)
    else:
        ans = 0
        i = 0

        while i < N:
            if initial[i] == final[i]:
                continue
            else:
                start = i + 1
                ans += 1
                if start < N:
                    while