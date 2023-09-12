# https://school.programmers.co.kr/learn/courses/30/lessons/120852
def solution(n):
    answer = []
    i = 2
    while i <= n:
        if n % i == 0:
            answer.append(i)
            n //= i
        else:
            i += 1
    return sorted(list(set(answer)))