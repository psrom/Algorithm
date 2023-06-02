# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12903
def solution(s):
    mid = (len(s)-1)//2
    
    if len(s) % 2 != 0:
        answer = s[mid]
    else:
        answer = s[mid:mid+2]
        
    return answer