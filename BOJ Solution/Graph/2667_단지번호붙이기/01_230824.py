# https://www.acmicpc.net/problem/2667
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(row, col):
    que = deque([(row, col)])
    graph[row][col] = 0
    cnt = 1

    while que:
        x, y = que.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
                que.append((nx, ny))
                graph[nx][ny] = 0
                cnt += 1

    return cnt


N = int(input())
graph = [list(map(int, (input()))) for _ in range(N)]

count_house = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            count_house.append(bfs(i, j))

count_house.sort()

print(len(count_house))
for cnt in count_house:
    print(cnt)
