# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12919
def solution(seoul):
    for idx, val in enumerate(seoul):
        if val == "Kim":
            return f"김서방은 {idx}에 있다"
