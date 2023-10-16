# https://school.programmers.co.kr/learn/courses/30/lessons/84512
def solution(word):
    answer = 0
    arr = [781, 156, 31, 6, 1]
    for i in range(len(word)):
        answer += "AEIOU".find(word[i]) * (arr[i]) + 1
        
    return answer