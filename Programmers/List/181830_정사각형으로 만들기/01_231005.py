# https://school.programmers.co.kr/learn/courses/30/lessons/181830
def solution(arr):
    r, c = len(arr), len(arr[0])
    m = abs(r - c)
    if r > c:
        for i in range(r):
            arr[i].extend([0] * m)
    elif r < c:
        for _ in range(m):
            arr.append([0] * c)
    return arr
