# https://www.acmicpc.net/problem/11725
def dfs(n):
    visit = set()
    visit.add(1)
    answer = [0 for _ in range(n)]

    stack = [1]
    while stack:
        p = stack.pop()
        for neighbor in graph[p]:
            if neighbor in visit:
                answer[p - 1] = neighbor
            else:
                visit.add(neighbor)
                stack.append(neighbor)
    ans = answer[1:]
    return ans


n = int(input())
graph = {i: [] for i in range(1, n + 1)}
for _ in range(n - 1):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

ans = dfs(n)
for a in ans:
    print(a)
