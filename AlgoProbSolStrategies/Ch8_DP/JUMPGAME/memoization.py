N = int(input())
graph = list(list(map(int, input().split())) for _ in range(N))
cache = [[-1] * N for _ in range(N)]


def jump(y, x):
    global cache, graph
    if y >= N or x >= N:
        return 0
    if y == N - 1 and x == N - 1:
        return 1

    if cache[y][x] != -1:
        return cache[y][x]

    jump_size = graph[y][x]

    ret = jump(y + jump_size, x) or jump(y, x + jump_size)
    cache[y][x] = ret

    return ret


print(jump(0, 0))
