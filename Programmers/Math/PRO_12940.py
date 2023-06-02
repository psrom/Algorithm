# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12940
def solution(n, m):
    answer = []
    gcd, lcm = 1, 1
    
    # 최대 공약수
    for i in range(1, min(n, m)+1):
        if n % i == 0 and m % i == 0:
            gcd = i
    answer.append(gcd)
    
    # 최소 공배수
    lcm = m * n // gcd
    answer.append(lcm)
    
    return answer

# 유클리드 호제법 이용
def solution2(n, m):
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    
    if n > m:
        n, m = m, n
        
    g = gcd(n, m)
    lcm = n * m // g
    
    answer = [g, lcm]
    
    return answer