# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/132267
# 문제를 처음에 너무 복잡하게 풀어서 다시 풀 것
def solution(a, b, n):
    answer = 0
    while n >= a:
        answer += (n // a) * b
        n = (n // a) * b + (n % a)
    return answer