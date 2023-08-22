# https://school.programmers.co.kr/learn/courses/30/lessons/155652
import string
def solution(s, skip, index):
    alphabets = [_ for _ in string.ascii_lowercase]
    
    # 뛰어넘을 글자들 미리 삭제
    for a in skip:
        alphabets.pop(alphabets.index(a))
    
    l = len(alphabets)
    answer = ''
    for i in s:
        idx = alphabets.index(i)
        new_idx = (idx + index) % l
        answer += alphabets[new_idx]
        
    return answer