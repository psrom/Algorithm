# https://school.programmers.co.kr/learn/courses/30/lessons/120850
def solution(my_string):
    answer = []
    for s in my_string:
        if s.isdigit():
            answer.append(int(s))
    return sorted(answer)