# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42889
from collections import Counter
def solution(N, stages):
    answer = []
    stages = Counter(stages)
    stages = sorted(stages.items())
    
    scores = dict()
    for i in range(N+1):
        scores[i+1] = 0
            
    for i in range(len(stages)):
        # 분모 구하기
        denominator = 0
        for j in range(i, len(stages)):
            denominator += stages[j][1]
            
        # 실패율 구하기: scores[스테이지] = 클리어X / 도달한 사람 수
        scores[stages[i][0]] = stages[i][1] / denominator
        
    sort_score = sorted(scores.items(), key = lambda x: x[1], reverse = True)
    
    if sort_score[0][0] == N+1:
        del sort_score[0]
        
    for i in range(N):
        answer.append(sort_score[i][0])
    
    return answer