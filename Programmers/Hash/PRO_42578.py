# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42578
def solution(clothes):
    answer = 1
    dic = dict()
    for cloth in clothes:
        if cloth[1] in dic:
            dic[cloth[1]] += 1
        else:
            dic[cloth[1]] = 1

    for i, v in dic.items():
        answer *= (v + 1)
    answer -= 1

    return answer