# https://www.acmicpc.net/problem/1919
from collections import Counter
first = input()
second = input()
if len(first) < len(second):
    first, second = second, first  # 더 긴 문자를 first로

first, second = Counter(first), Counter(second)
answer = 0
if first != second:
    for key, val in second.items():
        if key in first:
            answer += abs(first[key] - val)
            first.pop(key)
        else:
            answer += val

    if first:
        for val in first.values():
            answer += val

print(answer)