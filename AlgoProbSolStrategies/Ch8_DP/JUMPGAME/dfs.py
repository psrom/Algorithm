N = int(input())
graph = list(list(map(int, input().split())) for _ in range(N))
visited = [[0] * N for _ in range(N)]
dx = [0, 1]
dy = [1, 0]


def dfs(x, y):
    global graph
    if x == N - 1 and y == N - 1:
        return 1

    for i in range(2):
        nx = x + dx[i] * graph[x][y]
        ny = y + dy[i] * graph[x][y]

        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            visited[nx][ny] = 1
            if dfs(nx, ny):
                return 1
    return 0


print(dfs(0, 0))
