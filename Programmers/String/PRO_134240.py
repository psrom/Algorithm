# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/134240
def solution(food):
    answer = ''
    temp = ''
    for i in range(1, len(food)):
        if food[i] % 2 != 0:
            food[i] = food[i] - 1
        
        cal = food[i] // 2 # int형
        temp += str(i) * cal
        
    answer = temp + "0" + temp[::-1]
    
    return answer