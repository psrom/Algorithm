# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/70128
def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]
        
    return answer