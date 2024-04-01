# https://www.acmicpc.net/problem/7562
from collections import deque

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]


def bfs():
    while que:
        x, y, cnt = que.popleft()
        if (x, y) == (target_x, target_y):
            return cnt

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                visited[nx][ny] = True
                que.append((nx, ny, cnt + 1))


for _ in range(int(input())):
    l = int(input())
    x, y = map(int, input().split())
    target_x, target_y = map(int, input().split())

    graph = [[0] * (l + 1) for _ in range(l + 1)]
    que = deque([(x, y, 0)])
    visited = [[False] * (l + 1) for _ in range(l + 1)]
    print(bfs())
