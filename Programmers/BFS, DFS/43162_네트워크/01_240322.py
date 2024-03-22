# https://school.programmers.co.kr/learn/courses/30/lessons/43162
def dfs(n, computers, node, visited):
    visited[node] = True
    for i in range(n):
        if i != node and computers[i][node] == 1 and not visited[i]:
            dfs(n, computers, i, visited)


def solution(n, computers):
    answer = 0
    visited = [False] * n

    for i in range(n):
        if visited[i] == False:
            dfs(n, computers, i, visited)
            answer += 1

    return answer
