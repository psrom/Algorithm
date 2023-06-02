# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12917
def solution(s):
    ls = list(s)
    ls.sort(reverse = True)
    
    return "".join(ls)