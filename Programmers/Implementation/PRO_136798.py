# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/136798
def solution(number, limit, power):
    answer = 0
    
    knights = [i+1 for i in range(number)]
    
    divisor = []
    for knight in knights:
        cnt = 0
        for i in range(1, int(knight ** 0.5)+1): # 약수 개수 구하기
            if knight % i == 0:
                cnt += 1
                if (i != knight // i):
                    cnt += 1
            
        divisor.append(cnt)
    
    for i in range(len(divisor)): # limit을 넘어가는 경우 power로 대체
        if divisor[i] > limit:
            divisor[i] = power
            
    answer = sum(divisor)
    
    return answer