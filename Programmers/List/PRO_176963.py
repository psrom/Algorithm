# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/176963
def solution(name, yearning, photo):
    answer = []
    for image in photo:
        score = 0
        for people in image:
            if people in name:
                idx = name.index(people)
                score += yearning[idx]
        answer.append(score)
                
    return answer