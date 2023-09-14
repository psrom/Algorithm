# https://school.programmers.co.kr/learn/courses/30/lessons/92335
import math
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def calc(n, k):
    temp = ''
    while n > 0:
        n, mod = divmod(n, k)
        temp += str(mod)

    return temp[::-1]


def solution(n, k):
    numbers = calc(n, k)
    answer = 0
    for i in numbers.split("0"):
        if i.isdigit() and is_prime(int(i)):
            answer += 1

    return answer