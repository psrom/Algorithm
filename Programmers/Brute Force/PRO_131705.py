# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/131705
def solution(number):
    answer = 0
    l = len(number)
    
    for i in range(l-2):
        for j in range(i+1, l-1):
            for k in range(j+1, l):
                sum = number[i] + number[j] + number[k]
                if sum == 0:
                    answer += 1
    
    return answer