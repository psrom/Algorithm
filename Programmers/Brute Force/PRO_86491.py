# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/86491
def solution(sizes):
    w = [] # 큰 수
    h = [] # 작은 수
    for size in sizes:
        if size[0] > size[1]:
            w.append(size[0])
            h.append(size[1])
        else:
            w.append(size[1])
            h.append(size[0])
            
    answer = max(w) * max(h)
    
    return answer