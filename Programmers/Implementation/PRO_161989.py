# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/161989
def solution(n, m, section):
    answer = 0
    wall = [1 for i in range(n+1)]
            
    for i in section:
        wall[i] = 0 # 다시 칠해야 하는 부분
    
    for j in range(1, n+1):
        if wall[j] == 0:
            if j+m <= n:
                for k in range(j, j+m):
                    wall[k] = 1
            else:
                for k in range(j, n+1):
                    wall[k] = 1
            answer += 1
            
    return answer

# ========================================
def solution2(n, m, section):
    answer = 1
    prev = section[0]
    
    for element in section:
        if element - prev >= m:
            prev = element
            answer += 1

    return answer