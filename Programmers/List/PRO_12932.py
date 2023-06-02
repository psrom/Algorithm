# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12932
def solution(n):
    answer = []
    for i in str(n):
        answer.append(int(i))
    answer.reverse()
    return answer