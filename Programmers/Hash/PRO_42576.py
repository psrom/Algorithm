# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42576
def solution(participant, completion):
    answer = ""
    dic = {}

    for name in participant:
        if name in dic:
            dic[name] += 1
        else:
            dic[name] = 1

    for complete in completion:
        dic[complete] -= 1

    for idx, val in dic.items():
        if val != 0:
            answer += idx

    return answer