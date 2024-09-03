# https://www.acmicpc.net/problem/11403
from collections import deque

def bfs(graph, start, n):
    visited = [0] * n
    que = deque([start])
    
    while que:
        q = que.popleft()
        
        for neighbor in range(n):
            if graph[q][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = 1
                que.append(neighbor)
                
    return visited
    
        
def find_path(n, graph):
    result = []
    
    for i in range(n):
        result.append(bfs(graph, i, n))
        
    return result

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

result = find_path(n, graph)

for row in result:
    print(*row)
