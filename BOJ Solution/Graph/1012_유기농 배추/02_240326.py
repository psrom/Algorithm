# https://www.acmicpc.net/problem/1012
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(r, c):
    que = deque([(r, c)])
    graph[r][c] = 0
    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                que.append((nx, ny))


for _ in range(int(input())):
    M, N, K = map(int, input().split())
    graph = [[0] * N for _ in range(M)]
    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1

    ans = 0
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                bfs(i, j)
                ans += 1

    print(ans)
