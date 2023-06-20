# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/87390
def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        answer.append(max(i // n, i % n) + 1)

    return answer


def solution2(n, left, right): # 처음 풀이
    answer = []
    for i in range(left, right + 1):
        a = i // n  # 몫
        b = i % n  # 나머지
        if a < b:
            a, b = b, a
        answer.append(a + 1)

    return answer
