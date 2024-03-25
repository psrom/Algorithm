# https://www.acmicpc.net/problem/2667
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(start_x, start_y):
    que = deque([(start_x, start_y)])
    graph[start_x][start_y] = 0
    cnt = 1

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                que.append((nx, ny))
                cnt += 1

    return cnt


N = int(input())
graph = [list(map(int, input())) for _ in range(N)]

answer = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            answer.append(bfs(i, j))

answer.sort()

print(len(answer))
for a in answer:
    print(a)
