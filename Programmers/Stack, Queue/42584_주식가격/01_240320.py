# https://school.programmers.co.kr/learn/courses/30/lessons/42584
from collections import deque


def solution(prices):
    d = deque(prices)
    answer = []

    while d:
        p = d.popleft()
        cnt = 0
        if d:
            for i in d:
                if i >= p:
                    cnt += 1
                elif i < p:
                    cnt += 1
                    break
        answer.append(cnt)

    return answer
