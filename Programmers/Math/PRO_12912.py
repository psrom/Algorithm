# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12912
def solution(a, b):
    answer = 0

    if a >= b:
        a, b = b, a  # a가 항상 작도록

    for i in range(a, b + 1):
        answer += i

    return answer