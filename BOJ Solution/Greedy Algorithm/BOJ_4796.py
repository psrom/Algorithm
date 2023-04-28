# 문제: https://www.acmicpc.net/problem/4796
i = 1
while True:
    l, p, v = map(int, input().split())
    if (l, p, v) == (0, 0, 0):
        break

    cnt = v//p
    r = v%p
    if r <= l:
        print(f"Case {i}: {cnt*l + r}")
    else:
        print(f"Case {i}: {cnt*l + l}")
    i += 1