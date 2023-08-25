# https://www.acmicpc.net/problem/1697
from collections import deque

def bfs(start, target):
    que = deque([(start, 0)])
    visited = set([start])
    max_num = 100000

    while que:
        position, time = que.popleft()

        if position == target:
            return time

        if position - 1 >= 0 and position - 1 not in visited:
            que.append((position - 1, time + 1))
            visited.add(position - 1)

        if position + 1 <= max_num and position + 1 not in visited:
            que.append((position + 1, time + 1))
            visited.add(position + 1)

        if position * 2 <= max_num and position * 2 not in visited:
            que.append((position * 2, time + 1))
            visited.add(position * 2)


N, K = map(int, input().split())
result = bfs(N, K)
print(result)