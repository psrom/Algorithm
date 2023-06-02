# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12950?language=python3
def solution(arr1, arr2):
    row = len(arr1)
    column = len(arr1[0])
    answer = [[0 for i in range(column)] for j in range(row)]
    
    for i in range(row):
        for j in range(column):
            answer[i][j] = arr1[i][j]+arr2[i][j]
            
    return answer