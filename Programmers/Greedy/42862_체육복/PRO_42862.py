# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42862
def solution(n, lost, reserve):
    n_lost = set(lost) - set(reserve)
    n_reserve = set(reserve) - set(lost)
    
    for x in n_lost:
        if x - 1 in n_reserve:
            n_reserve.remove(x-1)

        elif x + 1 in n_reserve:
            n_reserve.remove(x+1)

        else:
            n -= 1

    return n 