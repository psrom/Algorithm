# https://school.programmers.co.kr/learn/courses/30/lessons/120924

def solution(common):
    a1, a2, a3 = common[:3]
    r1 = a2 - a1
    r2 = a3 - a2

    if r1 == r2:
        answer = common[-1] + r1
    else:
        r = a2 // a1
        answer = common[-1] * r

    return answer