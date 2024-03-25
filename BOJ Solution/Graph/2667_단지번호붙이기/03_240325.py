# https://www.acmicpc.net/problem/2667
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    global cnt
    graph[x][y] = 0
    cnt += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
            dfs(nx, ny)


N = int(input())
graph = [list(map(int, input())) for _ in range(N)]

answer = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            cnt = 0  # 초기화
            dfs(i, j)
            answer.append(cnt)

answer.sort()

print(len(answer))
for ans in answer:
    print(ans)
