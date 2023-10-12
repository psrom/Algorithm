# https://www.acmicpc.net/problem/16953
A, B = map(int, input().split())
cnt = 0

while B > A:
    if B % 2 == 0:
        B //= 2
    elif B % 10 == 1:
        B //= 10
    else:
        break
    cnt += 1

if B == A:
    print(cnt + 1)
else:
    print(-1)
