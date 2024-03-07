# https://www.acmicpc.net/problem/17298
# 16:50-17:32
import sys

input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().rstrip().split()))
ans = [-1] * N
stack = []

for i in range(N):
    while stack and lst[stack[-1]] < lst[i]:
        ans[stack.pop()] = lst[i]
    stack.append(i)

print(*ans)
