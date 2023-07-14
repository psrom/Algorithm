# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/64065
def solution(s):
    answer = []
    s = s[2:-2].split("},{") # 1. 맨 앞과 맨 뒤의 {{}} 지우고 중괄호 기준으로 split
    
    lst = []
    for i in s: lst.append(list(map(int, i.split(",")))) # 2. {}로 묶여있던 숫자들 정리
    lst.sort(key = len) # 3. 길이대로 sort => 첫번째 원소를 알기 위해
    
    answer = []
    for element in lst:
        for i in range(len(element)):
            if element[i] not in answer:
                answer.append(element[i])
            else:
                pass
    
    return answer