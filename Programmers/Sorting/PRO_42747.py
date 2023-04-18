# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42747#
def solution(citations):
    # [25, 8, 5, 3, 3] => 3; 3번 이상 인용된 논문이 3편 이상
    result = []
    for c in citations:
        cnt = 0
        for i in range(len(citations)):
            if c <= citations[i]:
                cnt += 1
        result.append(min(c, cnt))
    return max(result)
