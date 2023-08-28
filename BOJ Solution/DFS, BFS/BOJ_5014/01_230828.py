# https://www.acmicpc.net/problem/5014
from collections import deque


def bfs(S, G):
    que = deque([(S, 0)])
    visited = [False] * (F + 1)
    visited[S] = True

    while que:
        current, cnt = que.popleft()

        if current == G:
            return cnt

        up_button = current + U
        down_button = current - D

        if up_button <= F and not visited[up_button]:
            que.append((up_button, cnt + 1))
            visited[up_button] = True

        if down_button > 0 and not visited[down_button]:
            que.append((down_button, cnt + 1))
            visited[down_button] = True

    return "use the stairs"


F, S, G, U, D = map(int, input().split())

building = [0] * (F + 1)
building[S] = 1
building[G] = 2

print(bfs(S, G))