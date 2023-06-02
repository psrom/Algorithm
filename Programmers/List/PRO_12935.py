# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12935
def solution(arr):
    answer = []

    arr.remove(min(arr))
    answer = arr
    
    if not arr:
        answer = [-1]
    
    return answer