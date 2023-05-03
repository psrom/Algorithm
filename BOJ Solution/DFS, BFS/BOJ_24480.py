# 문제: https://www.acmicpc.net/problem/24480
# DFS 정복하기!

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 오름차순 탐색
visited_dfs = [0] * (n+1)
cnt = 1

def dfs(r):
    global cnt
    visited_dfs[r] = cnt
    graph[r].sort(reverse=True)
    for g in graph[r]:
        if visited_dfs[g] == 0:
            cnt += 1
            dfs(g)

dfs(r)
for i in range(1, n+1):
    print(visited_dfs[i])