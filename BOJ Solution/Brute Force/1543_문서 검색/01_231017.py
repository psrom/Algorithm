# https://www.acmicpc.net/problem/1543
from collections import deque

document = deque(list(input()))
target = deque(list(input()))
t_len = len(target)
temp = deque([])
cnt = 0

while document:
    p = document.popleft()
    temp.append(p)

    if len(temp) > t_len:
        temp.popleft()

    if temp == target:
        cnt += 1
        temp = deque([])

print(cnt)