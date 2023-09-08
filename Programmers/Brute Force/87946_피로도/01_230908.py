# https://school.programmers.co.kr/learn/courses/30/lessons/87946
import itertools
def solution(k, dungeons):
    nPr = itertools.permutations(dungeons, len(dungeons))
    answer = -1
    for p in nPr:
        result = 0
        hp = k
        for least_hp, spend_hp in p:
            if least_hp > hp:
                break
            hp -= spend_hp
            result += 1
        answer = max(answer, result)

    return answer