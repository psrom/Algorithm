# 문제: https://www.acmicpc.net/problem/9461
t = int(input())

for tc in range(t):
    n = int(input())
    p = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    if n<=10:
        print(p[n])
    else:
        for k in range(11, n+1):
            p.append(p[k-2]+p[k-3])
        print(p[n])
