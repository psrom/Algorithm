# https://school.programmers.co.kr/learn/courses/30/lessons/172928
def solution(park, routes):
    x, y = 0, 0
    H, W = len(park), len(park[0])
    for i in range(H):
        for j in range(W):
            if park[i][j] == "S":
                x, y = i, j

    op = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}

    for route in routes:
        d, n = route.split()
        dx, dy = x, y

        for i in range(int(n)):
            nx = x + op[d][0]
            ny = y + op[d][1]

            if 0 <= nx < H and 0 <= ny < W and park[nx][ny] != "X":
                x, y = nx, ny
            else:
                x, y = dx, dy
                break

    return [x, y]
