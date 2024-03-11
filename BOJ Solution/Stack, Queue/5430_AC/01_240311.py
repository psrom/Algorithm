# https://www.acmicpc.net/problem/5430
# 15:46-16:06/ 17:02-17:28
import sys
from collections import deque

input = sys.stdin.readline
for _ in range(int(input().rstrip())):
    p = str(input().rstrip())
    n = int(input().rstrip())
    lst = deque(list())
    if n == 0:
        x = input()
    else:
        x = input().rstrip().lstrip('[').rstrip(']').split(',')
        for i in x:
            lst.append(int(i))

    error = False
    check_direction = True
    for order in p:
        if order == "R":
            if check_direction:
                check_direction = False
            else:
                check_direction = True

        else:
            if not lst:
                error = True
                break
            else:
                if check_direction:
                    lst.popleft()
                else:
                    lst.pop()

    if error:
        print('error')
    else:
        if not check_direction:
            lst.reverse()

        ans = ''
        for i in lst:
            ans += str(i)
            ans += ','

        ans = '[' + ans[:-1] + ']'
        print(ans)
