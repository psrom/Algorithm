# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12921
def solution(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    answer = sum(primes)
    return answer
