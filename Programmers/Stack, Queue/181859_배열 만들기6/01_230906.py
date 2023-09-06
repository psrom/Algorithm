# https://school.programmers.co.kr/learn/courses/30/lessons/181859
def solution(arr):
    answer = []
    for i in range(len(arr)):
        if len(answer) == 0:
            answer.append(arr[i])
        elif len(answer) != 0:
            p = answer.pop()
            if p == arr[i]:
                pass
            else:
                answer.append(p)
                answer.append(arr[i])
    
    return answer if len(answer) > 0 else [-1]