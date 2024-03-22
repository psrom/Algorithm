# 문제: https://www.acmicpc.net/problem/2606
from collections import deque

n = int(input()) # 컴퓨터 수
v = int(input()) # 간선

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(v):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

Q = deque([1])
visited[1] = 1

while Q:
    c = Q.popleft()
    for node in graph[c]:
        if visited[node] == 0:
            Q.append(node)
            visited[node] = 1
print(sum(visited)-1)
