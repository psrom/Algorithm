# 문제: https://www.acmicpc.net/problem/2775
t = int(input())
for tc in range(t):
    k = int(input())
    n = int(input())

    apart = [[0]*n for _ in range(k+1)]
    for i in range(n): # 0층 i호 i명
        apart[0][i] = i+1
    for f in range(k+1):
        apart[f][0] = 1


    for i in range(1, k+1):
        for j in range(1, n):
            apart[i][j] = apart[i][j-1] + apart[i-1][j]

    print(apart[k][n-1])


