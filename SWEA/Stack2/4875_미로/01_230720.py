def dfs(maze, visited, x, y):
    if x < 0 or x >= N or y < 0 or y >= N or maze[y][x] == 1 or visited[y][x]:
        return False

    # 목적지에 도착한 경우
    if maze[y][x] == 3:
        return True

    # 현재 위치 방문 처리 후 DFS 탐색
    visited[y][x] = True

    if dfs(maze, visited, x + 1, y) or dfs(maze, visited, x - 1, y) or dfs(maze, visited, x, y + 1) or dfs(maze, visited, x, y - 1):
        return True

    # 현재 위치에서 더 이상 갈 수 있는 경로가 없는 경우
    # 현재 위치를 방문 가능한 상태로 변경하고 백트래킹 진행
    visited[y][x] = False
    return False


def find_path(maze):
    global N
    N = len(maze)
    visited = [[False for _ in range(N)] for _ in range(N)]

    start, end = None, None
    # 출발지와 도착지 위치 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = (j, i)
            elif maze[i][j] == 3:
                end = (j, i)

    if not start or not end:
        return "error"

    return 1 if dfs(maze, visited, start[0], start[1]) else 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    result = find_path(maze)
    print(f"#{tc} {result}")
