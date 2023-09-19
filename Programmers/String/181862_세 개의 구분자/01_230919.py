# https://school.programmers.co.kr/learn/courses/30/lessons/181862
def solution(myStr):
    
    answer = [s for s in myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ').split() if s]
    
    return answer if answer else ['EMPTY']