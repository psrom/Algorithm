# https://school.programmers.co.kr/learn/courses/30/lessons/181895
def solution(arr, intervals):
    answer = []
    for interval in intervals:
        s, e = interval[0], interval[1]
        for i in range(s, e + 1):
            answer.append(arr[i])
    return answer