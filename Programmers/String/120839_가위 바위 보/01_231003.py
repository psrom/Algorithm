# https://school.programmers.co.kr/learn/courses/30/lessons/120839
def solution(rsp):
    answer = ''
    for t in rsp:
        if t == '2':
            answer += '0'
        elif t == '0':
            answer += '5'
        elif t == '5':
            answer += '2'
    
    return answer