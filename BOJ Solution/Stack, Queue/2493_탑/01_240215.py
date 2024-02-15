# https://www.acmicpc.net/problem/2493
# 16:32-17:07
import sys

N = int(input())
tower = list(map(int, sys.stdin.readline().rstrip().split()))
stack = []
answer = []

for i in range(N):
    while stack:
        if stack[-1][1] > tower[i]:
            answer.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:
        answer.append(0)
    stack.append([i, tower[i]])

print(*answer)
