from math import ceil, floor

t = int(raw_input())

for r in range(t):
    s1 = raw_input().split()
    s1 = [int(x) for x in s1]
    n = s1[0]
    s = float(s1[1])
    y = float(s1[2])
    V = list(map(float,raw_input().split()))
    D = list(map(float,raw_input().split()))
    P = list(map(float,raw_input().split()))
    C = list(map(float,raw_input().split()))

    walking_time = n * (y / s)
    single_walk_time = y / s
    total_wait = 0
    time_past = 0

    for i in range(n):
        if(D[i] == 1):
            P[i] += time_past * V[i]
        else:
            P[i] -= time_past * V[i]
        if D[i] == 0 and P[i] <= pow(10,-6):
            if P[i] + C[i] < -pow(10,-6):
                time_past += single_walk_time
                continue
            else:
                final = P[i] + C[i]
                waiting_time = (final + pow(10,-6)) / abs(V[i])
                total_wait += waiting_time
                time_past += waiting_time + single_walk_time
        elif D[i] == 0 and P[i] > pow(10,-6):
            if single_walk_time < (P[i] - pow(10,-6)) / abs(V[i]):
                time_past += single_walk_time
                continue
            else:
                waiting_time = (P[i] + C[i] + pow(10,-6)) / abs(V[i])
                total_wait += waiting_time
                time_past += waiting_time + single_walk_time
        elif D[i] == 1 and P[i] < -pow(10,-6):
            if single_walk_time < (abs(P[i]) - pow(10,-6)) / V[i]:
                time_past += single_walk_time
                continue
            else:
                waiting_time = (abs(P[i]) + C[i] + pow(10,-6)) / V[i]
                total_wait += waiting_time
                time_past += waiting_time + single_walk_time
        elif D[i] == 1 and P[i] >= -pow(10,-6):
            if P[i] - C[i] > -pow(10,-6):
                time_past += single_walk_time
                continue
            else:
                final = P[i] - C[i]
                waiting_time = (pow(10,-6) - final) / abs(V[i])
                total_wait += waiting_time
                time_past += waiting_time + single_walk_time

    print(total_wait + walking_time)