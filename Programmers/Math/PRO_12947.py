# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12947
def solution(x):
    answer = True
    x_str = str(x)
    x_sum = 0
    for i in x_str:
        x_sum += int(i)

    # 조건식
    if x % x_sum != 0:
        answer = False

    return answer