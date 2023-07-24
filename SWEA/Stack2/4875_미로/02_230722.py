from collections import deque


def bfs(maze, start):
    N = len(maze)
    visited = [[False for _ in range(N)] for _ in range(N)]
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    q = deque()

    q.append(start)
    visited[start[0]][start[1]] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if maze[nx][ny] == 3:
                return True

            if maze[nx][ny] == 0 and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True

    return False


def find_path(maze):
    N = len(maze)
    start, end = None, None

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = (i, j)
            elif maze[i][j] == 3:
                end = (i, j)

    if not start or not end:
        return "error"

    return 1 if bfs(maze, start) else 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    print(f"#{tc} {find_path(maze)}")