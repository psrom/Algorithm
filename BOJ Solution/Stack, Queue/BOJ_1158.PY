# 요세푸스 문제: https://www.acmicpc.net/problem/1158
from collections import deque
n, k = map(int, input().split())

dq = deque([i for i in range(1, n+1)])
result = []

while dq:
    for i in range(k-1):
        rest = dq.popleft()
        dq.append(rest)
    r = dq.popleft()
    result.append(r)

print("<", end="")
for i in range(len(result)-1):
    print(result[i], end=", ")
print(str(result[-1])+">")