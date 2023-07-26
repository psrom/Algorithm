# https://school.programmers.co.kr/learn/courses/30/lessons/120907
def solution(quiz):
    answer = []
    for q in quiz:
        q = q.split()
        
        if q[1] == "+":
            cal = int(q[0]) + int(q[2])
            answer.append("O") if cal == int(q[-1]) else answer.append("X")
        else:
            cal = int(q[0]) - int(q[2])
            answer.append("O") if cal == int(q[-1]) else answer.append("X")
                    
    return answer