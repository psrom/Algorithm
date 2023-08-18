# https://school.programmers.co.kr/learn/courses/30/lessons/120843

def solution(numbers, k):
    return numbers[2 * (k - 1) % len(numbers)]
