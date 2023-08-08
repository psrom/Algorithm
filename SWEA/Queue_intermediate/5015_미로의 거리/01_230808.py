# import sys
# sys.stdin = open("sample_input.txt", "r")
from collections import deque
T = int(input())

# BFS 구현
def bfs(maze, start):
    visited = [[0 for _ in range(N)] for _ in range(N)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = True

    while q:
        x, y, dist = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            
            if maze[nx][ny] == 3:
                return dist
            
            if maze[nx][ny] == 0 and not visited[nx][ny]:
                q.append((nx, ny, dist + 1))
                visited[nx][ny] = True

    return 0


for test_case in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    # 시작점 찾기
    start = None
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = (i, j, 0)
    
    print(f"#{test_case} {bfs(maze, start)}")
    