# 문제: https://www.acmicpc.net/problem/2217
n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

lst.sort()
result = []

for i in range(len(lst)):
    r = lst[i]*(len(lst)-i)
    result.append(r)
print(max(result))
