# https://www.acmicpc.net/problem/2468
# 16:15-16:57
import sys

sys.setrecursionlimit(100_000)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def check(x, y, h):
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] > h and not visited[nx][ny]:
            visited[nx][ny] = 1
            check(nx, ny, h)


input = sys.stdin.readline
N = int(input())
graph = list(list(map(int, input().rstrip().split())) for _ in range(N))
result = 0

for k in range(max(map(max, graph))):
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] > k and not visited[i][j]:
                cnt += 1
                check(i, j, k)

    result = max(result, cnt)

print(result)
