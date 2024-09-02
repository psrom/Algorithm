# 기존 3진법 체계인 0, 1, 2로 계산하되
# 문자열 '124'를 매핑하여 문제에 맞게 답 출력

def solution(n):
    answer = ''
    
    while n > 0:
        # 0부터 인덱스 매핑 시작
        n -= 1
        answer = '124'[n % 3] + answer
        n //= 3
    
    return answer
