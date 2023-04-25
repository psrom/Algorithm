n = int(input())
dp = [0] * (n+1)

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    if i%2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1) # 기존, 1을 빼고 2로 나눈 경우 비교 후 업데이트
    if i%3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1) # 기존, 1을 빼고 3으로 나눈 경우 비교 후 업데이트

print(dp[n])