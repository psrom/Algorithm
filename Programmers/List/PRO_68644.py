#문제: https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            num = numbers[i] + numbers[j]
            answer.append(num)
            
    answer = sorted(set(answer))

    return answer