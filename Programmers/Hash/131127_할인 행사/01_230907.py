# https://school.programmers.co.kr/learn/courses/30/lessons/131127
from collections import Counter
def solution(want, number, discount):
    dic = dict(zip(want, number))
    
    answer = 0
    for i in range(len(discount) - 9):
        temp = Counter(discount[i: i + 10])
        if temp == dic:
            answer += 1
    
    return answer