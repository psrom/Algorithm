# https://school.programmers.co.kr/learn/courses/30/lessons/42626
import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    
    cnt = 0
    while len(scoville) >= 2:
        first = heapq.heappop(scoville)
        
        if first >= K:
            return cnt
        
        second = heapq.heappop(scoville)
        
        new_scoville = first + (second * 2)
        heapq.heappush(scoville, new_scoville)
        
        cnt += 1
    
    return cnt if scoville[0] >= K else -1