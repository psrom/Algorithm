# https://school.programmers.co.kr/learn/courses/30/lessons/43163
from collections import deque


def bfs(begin, target, words):
    que = deque()
    que.append([begin, 0])

    while que:
        curr, step = que.popleft()

        if curr == target:
            return step

        for word in words:
            cnt = 0
            for i in range(len(curr)):
                if word[i] != curr[i]:
                    cnt += 1

            if cnt == 1:
                que.append([word, step + 1])


def solution(begin, target, words):
    if target not in words:
        return 0

    return bfs(begin, target, words)
