# https://school.programmers.co.kr/learn/courses/30/lessons/49993
def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        temp = ''
        for s in skill_tree:
            if s in skill:
                temp += s
        if skill[:len(temp)] == temp:
            answer += 1

    return answer
