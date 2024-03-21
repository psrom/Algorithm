# https://school.programmers.co.kr/learn/courses/30/lessons/250121
def solution(data, ext, val_ext, sort_by):
    d = {'code': 0, 'date': 1, 'maximum': 2, 'remain': 3}

    answer = []
    for a in data:
        if a[d[ext]] < val_ext:
            answer.append(a)

    answer = sorted(answer, key=lambda x: x[d[sort_by]])

    return answer
