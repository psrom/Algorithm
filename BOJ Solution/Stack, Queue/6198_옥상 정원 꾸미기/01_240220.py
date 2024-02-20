# https://www.acmicpc.net/problem/6198
# 17:03-17:20
import sys

N = int(sys.stdin.readline().rstrip())
building = list(int(sys.stdin.readline().rstrip()) for _ in range(N))

stack = []
ans = 0
for b in building:
    while stack and stack[-1] <= b:
        stack.pop()
    stack.append(b)

    ans += len(stack) - 1

print(ans)
