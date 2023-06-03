# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/142086
def solution(s):
    answer = []
    dic = dict()
    
    for idx, val in enumerate(s):
        if val not in dic:
            dic[val] = idx
            answer.append(-1)
        else:
            answer.append(idx - dic[val])
            dic[val] = idx

    return answer