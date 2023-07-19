def dfs(start, end):
    visited[start] = 1
    if start == end:
        return 1

    for i in range(1, v + 1):
        if graph[start][i] and not visited[i]:
            if dfs(i, end):
                return 1
    return 0


T = int(input())
for tc in range(1, T + 1):
    v, e = map(int, input().split())
    graph = [[0 for _ in range(v + 1)] for _ in range(v + 1)]
    visited = [0 for _ in range(v + 1)]
    for _ in range(e):
        start, end = map(int, input().split())
        graph[start][end] = 1
    s, g = map(int, input().split())

    print(f"#{tc} {dfs(s, g)}")
