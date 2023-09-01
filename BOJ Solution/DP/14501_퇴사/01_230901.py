# https://www.acmicpc.net/problem/14501

N = int(input())
schedules = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (N + 1)

for i in range(N - 1, -1, -1):
    if i + schedules[i][0] <= N:
        dp[i] = max(schedules[i][1] + dp[i + schedules[i][0]], dp[i + 1])
    else:
        dp[i] = dp[i + 1]

print(dp[0])