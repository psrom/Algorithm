N = int(input())
graph = list(list(map(int, input().split())) for _ in range(N))


def jump(y, x):
    if y >= N or x >= N:
        return False

    if y == N - 1 and x == N - 1:
        return True

    jump_size = graph[y][x]
    return jump(y + jump_size, x) or jump(y, jump_size + x)


print(jump(0, 0))
