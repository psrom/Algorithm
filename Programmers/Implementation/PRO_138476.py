# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/138476
# =====================================================================
# >> from collections import Counter
# >> counter = Counter([n]])
# >> counter.most_common(2): val 개수를 큰 순서부터 2개 반환해줌
# none이면 모든 순서 반환
# 출력 예: [("a":3), ("b":5)]
# =====================================================================
from collections import Counter

def solution(k, tangerine):
    cnt = 0
    ans = 0

    counter = Counter(tangerine)

    for c in counter.most_common():
        cnt += c[1]
        ans += 1
        if cnt >= k:
            return ans
