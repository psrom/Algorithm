# https://school.programmers.co.kr/learn/courses/30/lessons/120840
def solution(balls, share):
    def factor(n):
        result = 1
        while n > 1:
            result *= n
            n -= 1
        return result
    
    answer = factor(balls) / (factor(balls - share) * factor(share))
    return answer