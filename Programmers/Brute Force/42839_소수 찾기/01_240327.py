# https://school.programmers.co.kr/learn/courses/30/lessons/42839
from itertools import permutations


def prime_numbers(n):
    arr = [True] * (n + 1)
    arr[0] = arr[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if arr[i]:
            for j in range(i * i, n + 1, i):
                arr[j] = False
    return arr


def solution(numbers):
    numbers = list(numbers)
    answer = []
    temp = []
    for i in range(1, len(numbers) + 1):
        temp += list(permutations(numbers, i))
    number_lst = set([int(("").join(j)) for j in temp])

    max_num = max(number_lst)
    ans = prime_numbers(max_num)

    for n in number_lst:
        if ans[n]:
            answer.append(n)

    return len(set(answer))
