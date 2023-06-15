# 문제: https://www.acmicpc.net/problem/2167
n, m = map(int, input().split())
memo = [[0] * (m+1) for _ in range(n+1)] # 0으로 채워진 리스트
arr = list(list(map(int, input().split())) for _ in range(n)) # 입력 받을 리스트

for i in range(1, n+1):
    for j in range(1, m+1):
        memo[i][j] = memo[i][j-1] + memo[i-1][j] - memo[i-1][j-1] + arr[i-1][j-1]

k = int(input())
for case in range(k):
    i, j, x, y = map(int, input().split())
    print(memo[x][y] - memo[i-1][y] - memo[x][j-1] + memo[i-1][j-1])