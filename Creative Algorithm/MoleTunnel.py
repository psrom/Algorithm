# 두더지굴

n = int(input()) # 가로 세로 크기

graph = [] # 2차원 배열로 그래프 입력
for _ in range(n):
    graph.append(list(map(int, input().split())))

def dfs(x, y):
    size = 1 # 두더지 굴의 크기
    graph[x][y] = 2
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n: # graph의 범위 내에 있는 경우 루프
            if graph[nx][ny] == 1:
                size += dfs(nx, ny)
    return size

tunnel_lst = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            tunnel_lst.append(dfs(i, j))
tunnel_lst.sort(reverse=True)

print(len(tunnel_lst))
for k in tunnel_lst:
    print(k)
