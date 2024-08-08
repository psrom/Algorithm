# https://www.acmicpc.net/problem/10974

def dfs():
    if len(lst) == N:
        print(*lst)
        return
    for i in range(1, N + 1):
        if i not in lst:
            lst.append(i)
            dfs()
            lst.pop()

N = int(input())            
lst = []
dfs()