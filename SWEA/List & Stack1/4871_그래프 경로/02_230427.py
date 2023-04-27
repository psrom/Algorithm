def dfs(start, end):
    visit[start] = 1
    if start == end:
        return 1

    for i in range(1, v+1):
        if graph[start][i] and not visit[i]: # 간선은 있지만 아직 방문하지 않은 노드
            if dfs(i, end): # 도착 노드를 찾은 경우
                return 1
    return 0

T = int(input())
for tc in range(1, T+1):
    v, e = map(int, input().split()) # 노드, 간선 개수

    graph = [[0 for _ in range(v+1)] for _ in range(v+1)]
    visit = [0 for _ in range(v+1)]

    for _ in range(e):
        i, j = map(int, input().split())
        graph[i][j] = 1
    s, g = map(int, input().split())

    print(f'#{tc} {dfs(s,g)}')
