# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12906
def solution(arr):
    answer = [arr[0]]
    
    for element in arr:
        if element != answer[-1]:
            answer.append(element)
        
    return answer