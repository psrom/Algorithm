# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12982
def solution(d, budget):
    answer = 0
    d.sort()
    
    for price in d:
        budget -= price
        answer += 1
        
        if budget < 0:
            answer -= 1
            break
    
    return answer