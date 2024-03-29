# https://www.acmicpc.net/problem/11725
from collections import deque


def bfs():
    while que:
        v = que.popleft()
        for node in graph[v]:
            if ans[node] == 0:
                ans[node] = v
                que.append(node)


n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

que = deque([1])
ans = [0] * (n + 1)

bfs()
answer = ans[2:]

for a in answer:
    print(a)
