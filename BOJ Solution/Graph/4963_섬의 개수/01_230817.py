# 섬의 개수: https://www.acmicpc.net/problem/4963
from collections import deque
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, -1, -1, 1]

def bfs(island, a, b):
    q = deque()
    q.append((a, b))
    island[a][b] = 0

    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= H or ny < 0 or ny >= W:
                continue
            if island[nx][ny] == 1:
                island[nx][ny] = 0
                q.append((nx, ny))


while True:
    W, H = map(int, input().split())
    if (W, H) == (0, 0):
        break

    else:
        island = []
        for _ in range(H):
            island.append(list(map(int, input().split())))

        cnt = 0
        for row in range(H):
            for col in range(W):
                if island[row][col] == 1:
                    bfs(island, row, col)
                    cnt += 1

        print(cnt)
