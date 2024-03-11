# https://www.acmicpc.net/problem/10866
# 14:49-15:02
import sys
from collections import deque

que = deque([])
for _ in range(int(input())):
    order = sys.stdin.readline().rstrip().split()

    if order[0] == 'push_front':
        que.appendleft(order[1])
    elif order[0] == 'push_back':
        que.append(order[1])
    elif order[0] == 'pop_front':
        print(-1) if not que else print(que.popleft())
    elif order[0] == 'pop_back':
        print(-1) if not que else print(que.pop())
    elif order[0] == 'size':
        print(len(que))
    elif order[0] == 'empty':
        print(0) if que else print(1)
    elif order[0] == 'front':
        print(-1) if not que else print(que[0])
    else:
        print(-1) if not que else print(que[-1])
