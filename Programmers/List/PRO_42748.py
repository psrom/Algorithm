# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42748
def solution(array, commands):
    answer = []
    
    for command in commands:
        sort_array = array[command[0]-1:command[1]]
        sort_array.sort()
        answer.append(sort_array[command[2]-1])
            
    return answer