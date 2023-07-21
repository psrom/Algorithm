# https://school.programmers.co.kr/learn/courses/30/lessons/181904
# 1) 구현
def solution(my_string, m, c):
    
    result = []
    for i in range(0, len(my_string), m):
        s = my_string[i:i + m]
        result.append(s)

    answer = ''
    for r in result:
        answer += r[c-1]
    
    return answer

# 2) 더 간단한 풀이
# return s[c-1::m]만 작성해도 원하는 결과 나옴