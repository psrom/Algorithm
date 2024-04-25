# https://www.acmicpc.net/problem/2583
from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    q.append((x, y))
    graph[x][y] = 1
    cnt = 1

    while q:
        r, c = q.popleft()

        for i in range(4):
            nx = r + dx[i]
            ny = c + dy[i]

            if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 0:
                q.append((nx, ny))
                graph[nx][ny] = 1
                cnt += 1
    return cnt


M, N, K = map(int, input().split())
graph = [[0] * N for _ in range(M)]
q = deque([])
ans = []

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            ans.append(bfs(i, j))

ans.sort()
print(len(ans))
print(*ans)
