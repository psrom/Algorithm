# https://school.programmers.co.kr/learn/courses/30/lessons/181851
def solution(rank, attendance):
    ranking = {}  # 학생 번호: 등수
    for i in range(len(rank)):
        if attendance[i] == True:
            ranking[i] = rank[i]
    
    ranking = sorted(ranking.items(), key=lambda x: x[1])
    a = ranking[0][0]
    b = ranking[1][0]
    c = ranking[2][0]
    
    answer = 10000 * a + 100 * b + c
    return answer