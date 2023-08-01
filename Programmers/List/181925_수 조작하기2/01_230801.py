# https://school.programmers.co.kr/learn/courses/30/lessons/181925
def solution(numLog):
    answer = ''
    for i in range(1, len(numLog)):
        temp = numLog[i - 1]
        if numLog[i] == (temp + 1):
            answer += 'w'
        elif numLog[i] == (temp - 1):
            answer += 's'
        elif numLog[i] == (temp + 10):
            answer += 'd'
        else:
            answer += 'a'
        
    return answer