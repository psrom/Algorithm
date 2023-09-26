# https://school.programmers.co.kr/learn/courses/30/lessons/120825
def solution(my_string, n):
    answer = ''
    for s in my_string:
        answer += s * n
        
    return answer