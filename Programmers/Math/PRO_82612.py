# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/82612
def solution(price, money, count):
    answer = 0
    need = 0
    for i in range(count):
        need += price * (i+1)
    
    answer = need - money
    if answer <= 0:
        return 0
    
    return answer