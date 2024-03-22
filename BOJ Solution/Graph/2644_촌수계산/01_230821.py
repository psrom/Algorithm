# https://www.acmicpc.net/problem/2644
from collections import deque


def bfs(graph, start, target):
    q = deque([(start, 0)])
    visited = [0] * (N + 1)
    cnt = 0

    while q:
        node, depth = q.popleft()
        visited[node] = 1

        if node == target:
            return depth

        for neighbor in graph[node]:
            if not visited[neighbor]:
                q.append((neighbor, depth + 1))
    return -1


N = int(input())
start, end = map(int, input().split())
graph = [[] for _ in range(N + 1)]

M = int(input())
for _ in range(M):
    parent, child = map(int, input().split())
    graph[parent].append(child)
    graph[child].append(parent)

result = bfs(graph, start, end)
print(result)
