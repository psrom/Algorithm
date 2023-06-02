# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12948
def solution(phone_number):
    l = len(phone_number)
    answer = "*" * (l - 4) + phone_number[l - 4:]

    return answer