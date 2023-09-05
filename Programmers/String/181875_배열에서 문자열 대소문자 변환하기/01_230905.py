# https://school.programmers.co.kr/learn/courses/30/lessons/181875
def solution(strArr):
    answer = []
    for i in range(len(strArr)):
        if i % 2 == 0:
            a = strArr[i].lower()
            answer.append(a)
        else:
            a = strArr[i].upper()
            answer.append(a)
        
    return answer