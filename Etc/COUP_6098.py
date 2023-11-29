# https://codeup.kr/problem.php?id=6098
graph = [list(map(int, input().split())) for _ in range(10)]
N = len(graph[0])
x, y = [1, 1]
graph[x][y] = 9

while True:
    if x == N - 1 and y == N - 1:
        break
    if graph[x][y] == 2:
        graph[x][y] = 9
        break

    y += 1
    if graph[x][y] == 1:
        x += 1
        y -= 1
        if graph[x][y] == 1:
            break
        elif graph[x][y] == 0:
            graph[x][y] = 9
    elif graph[x][y] == 0:
        graph[x][y] = 9

for row in graph:
    print(*row)
