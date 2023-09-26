# https://www.acmicpc.net/problem/14891
from collections import deque
gears = [deque(list(map(int, input()))) for _ in range(4)]


def left(num, direction):
    if num < 0:
        return
    if gears[num][2] != gears[num + 1][6]:
        left(num - 1, -direction)
        gears[num].rotate(direction)


def right(num, direction):
    if num > 3:
        return
    if gears[num][6] != gears[num - 1][2]:
        right(num + 1, -direction)
        gears[num].rotate(direction)


for _ in range(int(input())):
    num, direction = map(int, input().split())
    num -= 1
    left(num - 1, -direction)
    right(num + 1, -direction)
    gears[num].rotate(direction)

answer = 0
for i in range(4):
    answer += gears[i][0] * (2 ** i)

print(answer)