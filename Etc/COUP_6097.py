# https://codeup.kr/problem.php?id=6097
h, w = map(int, input().split())
graph = [[0 for _ in range(w)] for _ in range(h)]

for tc in range(int(input())):
    l, d, x, y = map(int, input().split())
    if d == 0:
        for j in range(y - 1, y - 1 + l):
            graph[x-1][j] = 1

    elif d == 1:
        for i in range(x - 1, x - 1 + l):
            graph[i][y - 1] = 1

for g in graph:
    print(*g)