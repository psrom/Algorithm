# https://www.acmicpc.net/problem/2178
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph, row, col):
    que = deque([(row, col, 1)])

    while que:
        row, col, distance = que.popleft()

        if row == N - 1 and col == M - 1:
            return distance

        for i in range(4):
            nx = row + dx[i]
            ny = col + dy[i]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                que.append((nx, ny, distance + 1))
                graph[nx][ny] = 0

    return -1


N, M = map(int, input().split())
graph = list(list(map(int, input())) for _ in range(N))
print(bfs(graph, 0, 0))
