# https://school.programmers.co.kr/learn/courses/30/lessons/154539
def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)

    for i, num in enumerate(numbers):
        while stack and numbers[stack[-1]] < num:
            answer[stack.pop()] = num
        stack.append(i)

    return answer
