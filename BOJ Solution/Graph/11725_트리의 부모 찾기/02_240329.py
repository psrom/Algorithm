# https://www.acmicpc.net/problem/11725
import sys
sys.setrecursionlimit(1_000_000) # 설정 안 해주면 오류 발생
def dfs(v):
    for i in graph[v]:
        if parent[i] == 0:
            parent[i] = v
            dfs(i)


n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    graph[i].append(j)
    graph[j].append(i)

parent = [0] * (n + 1)

dfs(1)

for v in range(2, n + 1):
    print(parent[v])
