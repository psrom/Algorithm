# https://www.acmicpc.net/problem/2583
import sys
sys.setrecursionlimit(10_000)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y, cnt):
    graph[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 0:
            cnt = dfs(nx, ny, cnt + 1)

    return cnt


M, N, K = map(int, input().split())
graph = list([0] * N for _ in range(M))

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for r in range(y1, y2):
        for c in range(x1, x2):
            graph[r][c] = 1

ans = []

for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            ans.append(dfs(i, j, 1))

ans.sort()
print(len(ans))
print(*ans)
