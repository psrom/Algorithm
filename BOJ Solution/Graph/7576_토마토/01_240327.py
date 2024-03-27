# https://www.acmicpc.net/problem/7576
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                visited[nx][ny] = True
                que.append((nx, ny))


M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
que = deque([])
answer = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            que.append((i, j))

bfs()
check = False
for row in graph:
    for col in row:
        if col == 0:
            print(-1)
            check = True
            break
    if check:
        break
    answer = max(answer, max(row))

if not check:
    print(answer - 1)
