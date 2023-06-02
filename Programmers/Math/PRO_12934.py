# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12934
import math

def solution(n):
    answer = 0
    sqrt = math.sqrt(n)
    trun = math.trunc(sqrt)

    cal = trun - sqrt  # 나머지가 있는지 확인하기 위해 연산
    if cal != 0:
        answer = -1
    else:
        answer = (sqrt + 1) ** 2

    return answer

# ====================================================
# %1을 이용하면 소수점 아래를 구할 수 있음
def solution2(n):
    answer = 0
    temp = math.sqrt(n)

    if temp % 1 != 0:
        answer = -1
    else:
        answer = (temp + 1) ** 2

    return answer