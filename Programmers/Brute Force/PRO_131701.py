# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/131701
def solution(elements):
    elements += elements  # 원소 반복
    s = set()

    for l in range(1, len(elements) // 2 + 1):
        for i in range(len(elements)):
            s.add(sum(elements[i:i + l]))  # 리스트의 합을 집합 s에 추가

    return len(s)