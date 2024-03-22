# https://www.acmicpc.net/problem/11724
from collections import deque
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True


def count_connect(graph):
    visited = [False] * (N + 1)
    cnt = 0

    for node in range(1, N + 1):
        if not visited[node]:
            bfs(graph, node, visited)
            cnt += 1

    return cnt


N, M = map(int,input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

result = count_connect(graph)
print(result)