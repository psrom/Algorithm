# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/138477
def solution(k, score):
    answer = []
    rank = []
    for i in score:
        rank.append(i)
        rank.sort(reverse=True)
        
        if len(rank) > k:
            del rank[-1]
            
        answer.append(rank[-1])
        
    return answer