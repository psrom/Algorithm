# https://school.programmers.co.kr/learn/courses/30/lessons/43165
from collections import deque
def solution(numbers, target):
    answer = 0
    que = deque([(0, 0)])
    
    while que:
        current_sum, idx = que.popleft()
        
        if idx == len(numbers):
            if current_sum == target:
                answer += 1
        else:
            que.append((current_sum + numbers[idx], idx + 1))
            que.append((current_sum - numbers[idx], idx + 1))
            
    return answer