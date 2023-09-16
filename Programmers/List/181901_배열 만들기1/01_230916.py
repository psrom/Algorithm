# https://school.programmers.co.kr/learn/courses/30/lessons/181901
def solution(n, k):
    
    answer = [i for i in range(k, n + 1, k)]
    
    return answer