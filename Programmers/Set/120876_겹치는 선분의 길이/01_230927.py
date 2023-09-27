# https://school.programmers.co.kr/learn/courses/30/lessons/120876

def solution(lines):
    sets = [set(range(min(l), max(l))) for l in lines]
    answer = len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])
    
    return answer