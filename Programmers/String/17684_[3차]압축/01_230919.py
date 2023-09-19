# https://school.programmers.co.kr/learn/courses/30/lessons/17684
import string
def solution(msg):
    alphabets = list(string.ascii_uppercase)
    answer = []
    
    w = ''
    i = 0
    while i < len(msg):
        w += msg[i]
        i += 1
        if i < len(msg) and w + msg[i] in alphabets:
            continue
        else:
            answer.append(alphabets.index(w) + 1)
            if i < len(msg):
                alphabets.append(w + msg[i])
            w = ''
    
    return answer