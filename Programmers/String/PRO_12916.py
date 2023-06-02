# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12916
def solution(s):
    answer = True
    s = s.lower()

    p_cnt, y_cnt = 0, 0
    for i in s:
        if i == "p":
            p_cnt += 1
        elif i == "y":
            y_cnt += 1
        else:
            continue

    if p_cnt != y_cnt:
        answer = False

    return answer

# .count() 이용한 solution
def solution2(s):
    s = s.lower()
    return False if s.count("p") != s.count("y") else True