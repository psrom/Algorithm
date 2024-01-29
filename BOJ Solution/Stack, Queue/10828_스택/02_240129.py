# https://www.acmicpc.net/problem/10828
# 20:39-20:45
import sys

stack = []
for _ in range(int(input())):
    order = sys.stdin.readline().rstrip().split()

    if order[0] == "push":
        stack.append(order[1])
    elif order[0] == "pop":
        if stack:
            print(stack.pop(-1))
        else:
            print(-1)
    elif order[0] == "size":
        print(len(stack))
    elif order[0] == "empty":
        print(0 if stack else 1)
    else:
        print(stack[-1] if stack else -1)
