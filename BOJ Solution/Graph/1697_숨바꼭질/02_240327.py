# https://acmicpc.net/problem/1697
# 최댓값 범위 주의하기
from collections import deque


def bfs():
    while que:
        x = que.popleft()
        if x == K:
            return graph[K]

        for nx in (x - 1, x + 1, 2 * x):
            if 0 <= nx <= m and not graph[nx]:
                graph[nx] = graph[x] + 1
                que.append(nx)


N, K = map(int, input().split())
m = 100_000
graph = [0] * (m + 1)
que = deque([N])

answer = bfs()
print(answer)
