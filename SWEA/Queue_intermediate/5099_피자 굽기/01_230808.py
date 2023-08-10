# 5099. [파이썬 S/W 문제해결 기본] 6일차 - 피자 굽기(D3)
# import sys
# sys.stdin = open("sample_input.txt", "r")
from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    pizza = deque([(i+1, cheese[i]) for i in range(M)])

    oven = deque()
    for _ in range(N):
        if pizza:
            oven.append(pizza.popleft())

    while len(oven) > 1:
        num, cheese_amount = oven.popleft()
        cheese_amount //= 2

        if cheese_amount > 0:
            oven.append((num, cheese_amount))
        elif pizza:
            oven.append(pizza.popleft())

    result = oven[0][0]

    print(f"#{test_case} {result}")
