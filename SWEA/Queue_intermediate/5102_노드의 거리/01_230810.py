# 5102. [파이썬 S/W 문제해결 기본] 6일차 - 노드의 거리(D2)
# import sys
# sys.stdin = open("sample_input.txt", "r")
from collections import deque

def bfs(graph, start, end):
    visited = set()
    queue = deque([(start, 0)])

    while queue:
        node, distance = queue.popleft()

        if node == end:
            return distance
        
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                queue.append((neighbor, distance + 1))

    return 0

T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    graph = {i: [] for i in range(1, V + 1)}

    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    S, G = map(int, input().split())
    result = bfs(graph, S, G)

    print(f"#{test_case} {result}")