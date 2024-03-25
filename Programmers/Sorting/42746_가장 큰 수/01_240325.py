# https://school.programmers.co.kr/learn/courses/30/lessons/42746
def solution(numbers):
    numbers = [str(i) for i in numbers]
    numbers.sort(key=lambda x: x * 3, reverse=True)

    answer = ''.join(numbers)
    return str(int(answer))
