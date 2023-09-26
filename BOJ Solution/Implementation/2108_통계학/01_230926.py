# https://www.acmicpc.net/problem/2108
# sys 라이브러리 미사용시 시간 초과
from collections import Counter
import sys
N = int(input())
numbers = [int(sys.stdin.readline()) for _ in range(N)]

# 1. 산술 평균: N개의 수들의 합을 N으로 나눈 값
average = round(sum(numbers) / N)

# 2. 중앙값: N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
numbers.sort()
median = numbers[N // 2]

# 3. 최빈값: N개의 수들 중 가장 많이 나타나는 값
number_counter = Counter(numbers)
max_cnt = max(number_counter.values())
most_common = [num for num, cnt in number_counter.items() if cnt == max_cnt]

# 최빈값이 2개 이상인 경우
if len(most_common) > 1:
    mode = most_common[1]
else:
    mode = most_common[0]

# 4. 범위: N개의 수들 중 최댓값과 최솟값의 차이
range_max_min = numbers[-1] - numbers[0]

print(average)
print(median)
print(mode)
print(range_max_min)