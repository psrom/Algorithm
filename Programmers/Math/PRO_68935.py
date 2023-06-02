# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/68935
def solution(n):
    tenary = ''
    answer = 0
    while n != 0:
        share = n//3
        res = n % 3
        tenary += str(res)
        
        n = n//3
        
    for i in range(len(tenary)):
        answer += int(tenary[i]) * (3 ** (len(tenary) - (i+1)))
        
        
    return answer

# ===============================================================
# str() 함수의 3진법 변환 이용

def solution2(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer