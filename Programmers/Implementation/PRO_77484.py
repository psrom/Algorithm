# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/77484
def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    
    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
            
    return rank[cnt_0 + ans],rank[ans]