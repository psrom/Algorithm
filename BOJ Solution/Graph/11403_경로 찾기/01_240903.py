# https://www.acmicpc.net/problem/11403
# 17:02 - 17:17

# floyd_warshall
# 모든 정점 쌍에 대한 경로 탐색
# N이 100 이하라 효과적(시간 복잡도: O(N^3))

def floyd(n, graph):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = 1

    return graph

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

result = floyd(n, graph)

for row in result:
    print(*row)