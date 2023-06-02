# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/147355
def solution(t, p):
    answer = 0
    for i in range(len(t)-len(p)+1):
        part_str = t[i:i+len(p)]
        if int(part_str) <= int(p):
            answer += 1
    
    return answer