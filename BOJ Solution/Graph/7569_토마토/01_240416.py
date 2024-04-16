# https://www.acmicpc.net/problem/7569
import sys
from collections import deque

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs():
    while que:
        x, y, z = que.popleft()

        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]

            if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M:
                if graph[nx][ny][nz] == 0:
                    graph[nx][ny][nz] = graph[x][y][z] + 1
                    que.append((nx, ny, nz))


M, N, H = map(int, input().split())
graph = list(list(list(map(int, sys.stdin.readline().split())) for _ in range(N)) for _ in range(H))
que = deque([])

# 익은 토마토 que에 입력
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                que.append((i, j, k))

bfs()

ans = 0
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        ans = max(ans, max(j))

print(ans - 1)
