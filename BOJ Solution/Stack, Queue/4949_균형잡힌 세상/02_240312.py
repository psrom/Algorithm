# https://www.acmicpc.net/problem/4949
import sys

input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == '.':
        break

    stack = []
    check = True
    for b in s:
        if b == '(' or b == '[':
            stack.append(b)
        elif b == ')':
            if not stack or stack[-1] == '[':
                check = False
                break
            elif stack[-1] == '(':
                stack.pop()

        elif b == ']':
            if not stack or stack[-1] == '(':
                check = False
                break
            elif stack[-1] == '[':
                stack.pop()

    if check and not stack:
        print('yes')
    else:
        print('no')
