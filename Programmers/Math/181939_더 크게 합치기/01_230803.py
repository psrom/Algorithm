# https://school.programmers.co.kr/learn/courses/30/lessons/181939
def solution(a, b):
    str_a, str_b = str(a), str(b)
    return max(int(str_a + str_b), int(str_b + str_a))
