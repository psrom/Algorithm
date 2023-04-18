# 문제: https://www.acmicpc.net/problem/2606
n = int(input())
v = int(input())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(v):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

def dfs(v):
    visited[v] = 1
    for nx in graph[v]:
        if visited[nx] == 0:
            dfs(nx)
dfs(1)
print(sum(visited)-1)