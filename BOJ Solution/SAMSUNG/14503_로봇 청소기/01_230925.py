# https://www.acmicpc.net/problem/14503
from collections import deque
N, M = map(int, input().split())
R, C, D = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def clean():
    cnt = 0
    que = deque([(R, C, D)])

    while que:
        r, c, d = que.popleft()

        if graph[r][c] == 0:
            graph[r][c] = 2
            cnt += 1

        clean_check = 0
        for _ in range(4):
            nd = (d + 3) % 4
            nx = r + dx[nd]
            ny = c + dy[nd]

            if graph[nx][ny] == 0:
                que.append((nx, ny, nd))
                break
            else:
                d = nd
                clean_check += 1

        if clean_check == 4:
            back = (d + 2) % 4
            nx = r + dx[back]
            ny = c + dy[back]

            if graph[nx][ny] != 1:
                que.append((nx, ny, d))
            else:
                return cnt

    return cnt


print(clean())