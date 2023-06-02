# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    temp = list(str(n))
    temp.sort(reverse=True)
    
    return int("".join(temp))