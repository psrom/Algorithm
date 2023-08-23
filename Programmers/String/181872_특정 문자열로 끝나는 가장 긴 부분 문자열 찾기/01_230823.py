# https://school.programmers.co.kr/learn/courses/30/lessons/181872
def solution(myString, pat):
    idx_pat = []
    for i in range(0, len(myString) - len(pat) + 1):
        if myString[i:i+len(pat)] == pat:
            idx_pat.append(i + len(pat))
    
    return myString[:idx_pat[-1]]