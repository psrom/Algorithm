# https://www.acmicpc.net/problem/1021
# 15:05-15:34
from collections import deque

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
dq = deque([i for i in range(1, N + 1)])
ans = 0


def pop_front(target, dq):
    f_lst = dq.copy()
    f_cnt = 0
    while f_lst[0] != target:
        p = f_lst.popleft()
        f_lst.append(p)
        f_cnt += 1
    return f_cnt, f_lst


def pop_back(target, dq):
    b_lst = dq.copy()
    b_cnt = 0
    while b_lst[0] != target:
        p = b_lst.pop()
        b_lst.appendleft(p)
        b_cnt += 1
    return b_cnt, b_lst


for n in numbers:
    f_cnt, f_lst = pop_front(n, dq)
    b_cnt, b_lst = pop_back(n, dq)

    if f_cnt <= b_cnt:
        ans += f_cnt
        dq = f_lst
    else:
        ans += b_cnt
        dq = b_lst
    dq.popleft()

print(ans)
