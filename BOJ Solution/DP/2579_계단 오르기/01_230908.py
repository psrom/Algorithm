# https://www.acmicpc.net/problem/2579
N = int(input())
stairs = [0]
for _ in range(N):
    stairs.append(int(input()))

if N == 1:
    print(stairs[1])
elif N == 2:
    print(stairs[1] + stairs[2])
else:
    dp = [0] * (N + 1)
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]

    for i in range(3, N + 1):
        dp[i] = max(dp[i - 2] + stairs[i], dp[i - 3] + stairs[i - 1] + stairs[i])

    print(dp[N])