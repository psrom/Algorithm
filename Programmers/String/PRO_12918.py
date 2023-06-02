# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12918
def solution(s):
    answer = True
    # condition 1: 문자열의 길이 확인
    if not (len(s) == 4 or len(s) == 6):
        answer = False
        
    # condition 2: 숫자로만 구성 되어있는지 확인
    if s.isdigit() == False:
        answer = False
        
    return answer