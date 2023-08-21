# https://school.programmers.co.kr/learn/courses/30/lessons/140108
def solution(s):
    count_x, count_not_x = 0, 0
    answer = 0
    
    for i in s:
        if count_x == count_not_x:
            answer += 1
            temp = i
        if temp == i:
            count_x += 1
        else:
            count_not_x += 1
    
    return answer