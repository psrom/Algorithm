# https://school.programmers.co.kr/learn/courses/30/lessons/120912

# [간단한 풀이]
# def solution(array):
#     return str(array).count('7')

def solution(array):
    s = ''
    for a in array:
        s += str(a)
    answer = s.count('7')
    return answer