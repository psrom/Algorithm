# https://school.programmers.co.kr/learn/courses/30/lessons/42577
# 정확성은 다 맞았지만, 효율성에서 낙 => 이중 for문, min 함수가 문제
# for문을 최소화 하고, 내장 함수 사용을 조심할 것
def solution(phone_book):
    answer = True
    
    for i in range(len(phone_book)-1):
        for j in range(i+1, len(phone_book)):
            m = min(len(phone_book[i]), len(phone_book[j]))
            if phone_book[i][:m] == phone_book[j][:m]:
                answer = False
                break
            else:
                continue
                
        
    return answer