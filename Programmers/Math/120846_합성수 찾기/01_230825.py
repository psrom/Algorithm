# https://school.programmers.co.kr/learn/courses/30/lessons/120846
def solution(n):
    arr = [False] * (n + 1)
    
    for i in range(2, n + 1):
        if arr[i] == False:
            j = 2
            
            while (i * j) <= n:
                arr[i * j] = True
                j += 1

    return sum(arr)
